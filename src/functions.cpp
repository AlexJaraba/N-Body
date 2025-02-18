#include "functions.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>
#include <unistd.h>
#include <time.h>
#define DRIFT_FAIL -1
#define DRIFT_SUCCESS 0
#define PI ((double) 3.14159265358979323846264338327950288419716939937510)

double F(double E, double e, double M) {
	/* F(E) = E - e*sin(E) - M */
	return E - e*sin(E) - M;
}

double Fp(double E, double e){
	/* derivative of the above 
	 * F'(E) = 1 - e*cos(E) */
	return 1 - e*cos(E);
}

double Fpp(double E, double e) {
	/* second derivative of F 
	 * F''(E) = e*sin(E) */
	return e*sin(E);
}

double Fppp(double E, double e) {
	/* third derivative of F 
	 * F'''(E) = e*cos(E) */
	return e*cos(E);
}

static double dsignum(double x){
	if (x>0) return 1.0;
	else return -1.0;
}

double E_from_M_e(double M, double e){
	/* extension of Halley's method, based on Danby eq. 6.6.7*/
	double tol = 2e-6;
	double E, dE1, dE2, dE3;
	double f, fp, fpp, fppp;
//	int niter;

	E = M + dsignum(sin(M))*0.85*e;
//	niter = 0;
	do {
		f = F(E, e, M);
		fp = Fp(E, e);
		fpp = Fpp(E, e);
		fppp= Fppp(E, e);

		dE1 = -f/fp;
		dE2 = -f/(fp+1/2.0*dE1*fpp);
		dE3 = -f/(fp+1/2.0*dE2*fpp+1/6.0*dE2*dE2*fppp);
		E += dE3;
//		niter++;
	} while (fabs(dE3) > tol) ;

//	printf(" %d ", niter);
	return E;
}