function vector_operations()
    clc;
    disp('Welcome to the Vector Operations Program');
    disp('Please choose an operation:');
    disp('1. Vector Addition');
    disp('2. Vector Subtraction');
    disp('3. Element-wise Vector Multiplication');
    disp('4. Scalar Multiplication');
    disp('5. Cross Product (3D only)');
    disp('6. Dot Product');
    disp('7. Plot Vectors');
    disp('8. Exit');

    choice = input('Enter your choice (1-8): ');

    switch choice
        case 1
            vector_addition();
        case 2
            vector_subtraction();
        case 3
            vector_multiplication();
        case 4
            vector_scalar_multiplication();
        case 5
            vector_cross_product();
        case 6
            vector_dot_product();
        case 7
            vector_plot();
        case 8
            disp('Exiting the program...');
            return;
        otherwise
            disp('Invalid choice. Please select a valid option.');
            vector_operations();  % Recursively call the function again
    end
end
