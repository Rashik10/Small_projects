% Define the number of cities
n = 6;

% Time required to travel between cities (in minutes)
T = [ 0 10 20 30 30 20;
     10  0 25 35 30 20;
     20 25  0 15 35 25;
     30 35 15  0 15 10;
     30 30 35 15  0 14;
     20 20 25 10 14  0];

% Define the coverage matrix
% If the travel time between city i and city j is <= 15 minutes, 
% city j can be covered by a fire station in city i.
coverage = T <= 15;

% Decision variable: x(i) = 1 if a fire station is built in city i, otherwise 0
% Objective function: minimize sum(x)
f = ones(n, 1);  % This is the coefficient for the objective function (minimize number of fire stations)

% Constraints: Ensure every city is covered by at least one fire station
A = -coverage;  % Negative because we use <= constraints
b = -ones(n, 1);  % Every city must be covered by at least one fire station

% Define the bounds and integer constraints for binary variables
lb = zeros(n, 1);  % Lower bound: 0 (no fire station)
ub = ones(n, 1);   % Upper bound: 1 (fire station exists)
intcon = 1:n;      % Indices of integer variables

% Solve the integer linear programming problem
[x_opt, fval] = intlinprog(f, intcon, A, b, [], [], lb, ub);

% Display the results
fprintf('The optimal number of fire stations is: %d\n', fval);
disp('Fire stations should be built in the following cities:');
for i = 1:n
    if x_opt(i) == 1
        fprintf('City %d\n', i);
    end
end
