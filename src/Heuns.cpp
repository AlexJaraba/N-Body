#include "integrator.h"
#include "body.h"
#include <vector>
#include <cstddef>

void Heuns::step(std::vector<Body>& bodies, double dt) {
    // Store initial positions, velocities, and accelerations
    std::vector<std::vector<double>> initial_positions(bodies.size(), std::vector<double>(3));
    std::vector<std::vector<double>> initial_velocities(bodies.size(), std::vector<double>(3));
    std::vector<std::vector<double>> initial_accelerations(bodies.size(), std::vector<double>(3));

    // Store initial positions and velocities
    for (size_t i = 0; i < bodies.size(); ++i) {
        for (int j = 0; j < 3; ++j) {
            initial_positions[i][j] = bodies[i].position[j];
            initial_velocities[i][j] = bodies[i].velocity[j];
        }
    }

    // Compute initial accelerations
    for (auto& body : bodies) {
        body.updateAcceleration(bodies);
    }

    // Store initial accelerations
    for (size_t i = 0; i < bodies.size(); ++i) {
        for (int j = 0; j < 3; ++j) {
            initial_accelerations[i][j] = bodies[i].acceleration[j];
        }
    }

    // Perform Euler step
    for (size_t i = 0; i < bodies.size(); ++i) {
        for (int j = 0; j < 3; ++j) {
            bodies[i].position[j] += dt * initial_velocities[i][j];
            bodies[i].velocity[j] += dt * initial_accelerations[i][j];
        }
    }

    // Compute new accelerations after Euler step
    for (auto& body : bodies) {
        body.updateAcceleration(bodies);
    }

    // Correct step using Heun's method
    for (size_t i = 0; i < bodies.size(); ++i) {
        for (int j = 0; j < 3; ++j) {
            bodies[i].position[j] = initial_positions[i][j] + 0.5 * dt * (initial_velocities[i][j] + bodies[i].velocity[j]);
            bodies[i].velocity[j] = initial_velocities[i][j] + 0.5 * dt * (initial_accelerations[i][j] + bodies[i].acceleration[j]);
        }
    }
}
