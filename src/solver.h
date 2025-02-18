#ifndef SOLVER_H
#define SOLVER_H

#include <vector>
#include "body.h"
#include "integrator.h"
#include "functions.h"

class Solver {
public:
    Solver(std::vector<Body>& bodies);
    ~Solver();
    void run(int steps, double dt);

private:
    std::vector<Body>& bodies;
    Integrator* integrator;
};

#endif // SOLVER_H

