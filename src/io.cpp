#include "io.h"
#include "globals.h"
#include "solver.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>

void readInitialConditions(const std::string& filename, std::vector<Body>& bodies) {
    std::ifstream infile(filename);
    if (!infile) {
        std::cerr << "Error: Could not open file " << filename << std::endl;
        return;
    }

    std::string line;
    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        double mass;
        std::vector<double> position(3), velocity(3);

        if (!(iss >> mass >> position[0] >> position[1] >> position[2] 
                   >> velocity[0] >> velocity[1] >> velocity[2])) {
            std::cerr << "Error: Invalid format in line: " << line << std::endl;
            continue;  // Skip to the next line
        }

        bodies.emplace_back(mass, position, velocity);
    }

    std::cout << "Number of bodies read: " << bodies.size() << std::endl;
}

void writeOutput(const std::string& filename, const std::vector<Body>& bodies, double time) {
    std::ofstream outfile(filename, std::ios_base::app);  // Append to the file

    if (!outfile) {
        std::cerr << "Error: Could not open file " << filename << " for writing!\n";
        return;
    }

    outfile << time;  // Start with the current time

    for (const auto& body : bodies) {
        outfile << " " << body.mass;
        for (const auto& pos : body.position) outfile << " " << pos;
        for (const auto& vel : body.velocity) outfile << " " << vel;
    }
    outfile << "\n";  // Newline at the end of each timestep

    outfile.close();
}

void get_dimensions(const std::string& filename, int& nlines, int& ncols) {
    std::ifstream infile(filename);
    if (!infile.is_open()) {
        std::cerr << "Unable to open file: " << filename << std::endl;
        return;
    }

    std::string line;
    nlines = 0;
    ncols = 0;

    while (std::getline(infile, line)) {
        nlines++;
        std::istringstream iss(line);
        std::string word;
        int cols_in_line = 0;
        while (iss >> word) {
            cols_in_line++;
        }
        if (cols_in_line > ncols) {
            ncols = cols_in_line;
        }
    }

    infile.close();
}

void read_data(const std::string& filename, std::vector<std::vector<double>>& data, int nlines, int ncols) {
    std::ifstream infile(filename);
    if (!infile.is_open()) {
        std::cerr << "Unable to open file: " << filename << std::endl;
        return;
    }

    data.resize(nlines, std::vector<double>(ncols, 0.0));
    std::string line;
    int row = 0;

    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        int col = 0;
        double value;
        while (iss >> value) {
            data[row][col] = value;
            col++;
        }
        row++;
    }

    infile.close();
}

void writeEnergy(const std::string& filename, const std::string& filename_params, const std::string& output_filename) {
    // Open the input file
    std::ifstream infile(filename);
    if (!infile.is_open()) {
        std::cerr << "Unable to open file: " << filename << std::endl;
        return;
    }

    int nlines = 0;
    int nbodies = 0;

    std::string line;
    std::getline(infile, line); // Read the first line to get nlines and nbodies
    std::istringstream iss(line);
    iss >> nlines >> nbodies;

    // Declare vectors to hold the data
    std::vector<double> masses(nbodies);
    std::vector<std::vector<double>> x(nlines, std::vector<double>(nbodies));
    std::vector<std::vector<double>> y(nlines, std::vector<double>(nbodies));
    std::vector<std::vector<double>> z(nlines, std::vector<double>(nbodies));
    std::vector<std::vector<double>> vx(nlines, std::vector<double>(nbodies));
    std::vector<std::vector<double>> vy(nlines, std::vector<double>(nbodies));
    std::vector<std::vector<double>> vz(nlines, std::vector<double>(nbodies));

    // Read masses
    std::getline(infile, line);
    iss.clear();
    iss.str(line);
    for (int i = 0; i < nbodies; ++i) {
        iss >> masses[i];
    }

    // Read the rest of the data
    for (int i = 0; i < nlines; ++i) {
        for (int j = 0; j < nbodies; ++j) {
            infile >> x[i][j] >> y[i][j] >> z[i][j] >> vx[i][j] >> vy[i][j] >> vz[i][j];
        }
    }
    infile.close();

    // Read params
    SolverParams params = readParams(filename_params);
    double G = params.gravitational_constant;

    // Energy Calculation
    std::vector<double> Kinetic(nlines, 0.0);
    std::vector<double> Potential(nlines, 0.0);
    std::vector<double> M(nlines, 0.0);
    std::vector<double> M_rel(nlines, 0.0);

    for (int i = 0; i < nlines; ++i) {
        for (int j = 0; j < nbodies; ++j) {
            double v = (vx[i][j] * vx[i][j]) + (vy[i][j] * vy[i][j]) + (vz[i][j] * vz[i][j]);
            double K = 0.5 * masses[j] * v;
            Kinetic[i] += K;
            for (int k = j + 1; k < nbodies; ++k) {
                double r = ((x[i][j] - x[i][k]) * (x[i][j] - x[i][k])) +
                           ((y[i][j] - y[i][k]) * (y[i][j] - y[i][k])) +
                           ((z[i][j] - z[i][k]) * (z[i][j] - z[i][k]));
                double U = (-1 * G * masses[k] * masses[j]) / std::sqrt(r);
                Potential[i] += U;
            }
        }
    }

    for (int i = 0; i < nlines; ++i) {
        M[i] = Potential[i] + Kinetic[i];
    }

    for (int i = 0; i < nlines; ++i) {
        M_rel[i] = std::abs((M[i] - M[0]) / M[0]);
    }

    // Write M_rel to a separate text file
    std::ofstream outfile(output_filename);
    if (outfile.is_open()) {
        for (const auto& value : M_rel) {
            outfile << value << std::endl;
        }
        outfile.close();
    } else {
        std::cerr << "Unable to open file for writing!" << std::endl;
    }
}

SolverParams readParams(const std::string& filename) {
    std::ifstream infile(filename);
    std::string line, param;
    SolverParams params = {100, 10.0, 0.01, "leapfrog", 6.67430e-11};  // Default values


    while (std::getline(infile, line)) {
        std::istringstream iss(line);
        if (iss >> param) {
            if (param == "output_frequency") {
                iss >> params.output_frequency;
            } else if (param == "runtime") {
                iss >> params.runtime;
            } else if (param == "timestep") {
                iss >> params.timestep;
            } else if (param == "integrator") {
                iss >> params.integrator;
            } else if (param == "gravitational_constant") {
	            iss >> params.gravitational_constant;
        }
    }}

    return params;
}
