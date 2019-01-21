
# pystan base model

base_model = """

data {


}

parameters {


}


model {


}

"""


# pystan model for Linear Regression

'''
Notes for linear regression

The simplest form of the linear regression model with simple predictor and a slope and intercept coefficient, are 
normally distributed. The model can be written using standard regression notation as

 y[n] = alpha + beta x[n] + epsilon[n]  where   epsilon[n] ~ normal(0, sigma)
 
 
 we can also write the above equation as 
 
 y[n] ~ Normal(alpha + beta * x[n], sigma)

'''


linear_regression = """

data{
    int<lower=0> N;
    vector[N] x;
    vector[N] y;
}


parameters{
    real alpha;
    real beta;
    real <lower=0> sigma;
}


model {
    y ~ Normal(alpha+beta*x, sigma);
}

"""