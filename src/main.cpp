#include <iostream>
#include <vector>    // Correct inclusion of vector header
#include <string>    // Correct inclusion of string header
#include "body.h"
#include "solver.h"
#include "io.h"
#include "globals.h"

int main() {
    std::vector<Body> bodies;
    readInitialConditions("data/initial_conditions.txt", bodies);

    Solver sim(bodies);
    SolverParams params = readParams("data/param.txt");
    int steps = static_cast<int>(params.runtime / params.timestep);
    sim.run(steps, params.timestep);  // Use runtime and timestep from params

    return 0;
}
