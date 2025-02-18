#include "solver.h"
#include "integrator.h"
#include "io.h"
#include "globals.h"
#include "functions.h"
#include <iostream>

Solver::Solver(std::vector<Body>& bodies) : bodies(bodies), integrator(nullptr) {
    SolverParams params = readParams("data/param.txt");

    if (params.integrator == "leapfrog") {
        integrator = new Leapfrog();
    }

    if (params.integrator == "Heuns") {
        integrator = new Heuns();
    }
    // Add more integrator options here as needed
}

Solver::~Solver() {
    delete integrator;
}

void Solver::run(int steps, double dt) {
    std::cerr << "Solver::run() started with " << steps << " steps\n";

    SolverParams params = readParams("data/param.txt");

    int output_frequency = params.output_frequency;
    double runtime = params.runtime;
    dt = params.timestep;
    steps = static_cast<int>(runtime / dt);
    G = params.gravitational_constant;  // Set the global gravitational constant

    std::cerr << "Number of bodies: " << bodies.size() << "\n";

    for (int step = 0; step < steps; ++step) {
        integrator->step(bodies, dt);
        // Write output at the specified frequency
        if (step % output_frequency == 0 || step < 10) {
	        writeOutput("data/output.txt", bodies, step * dt);
        }
    }
    // Write final output
    writeOutput("data/output.txt", bodies, steps * dt);
    //writeEnergy("data/Energy_output.txt","data/param.txt");
}

