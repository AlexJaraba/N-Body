#include "solver.h"
#include "integrator.h"
#include "io.h"
#include "globals.h"
#include <iostream>

Solver::Solver(std::vector<Body>& bodies) : bodies(bodies), integrator(nullptr) {
    SolverParams params = readParams("data/param.txt");

    if (params.integrator == "leapfrog") {
        integrator = new Leapfrog();
    }
    // Add more integrator options here as needed
}

Solver::~Solver() {
    delete integrator;
}

void Solver::run(int steps, double dt) {
    SolverParams params = readParams("data/param.txt");

    int output_frequency = params.output_frequency;
    double runtime = params.runtime;
    dt = params.timestep;
    steps = static_cast<int>(runtime / dt);
    G = params.gravitational_constant;  // Set the global gravitational constant


    for (int step = 0; step < steps; ++step) {
        integrator->step(bodies, dt);
        // Write output at the specified frequency
        if (step % output_frequency == 0) {
	  writeOutput("data/output.txt", bodies, step * dt);
        }
    }

    // Write final output
    writeOutput("data/output.txt", bodies, steps * dt);
}

