function matrix_operations()
    clc;
    disp('Welcome to the Matrix Operations Program');
    disp('Please choose an operation:');
    disp('1. Addition');
    disp('2. Subtraction');
    disp('3. Multiplication');
    disp('4. Division');
    disp('5. Inverse');
    disp('6. Determinant');
    disp('7. Exit');

    choice = input('Enter your choice (1-7): ');

    switch choice
        case 1
            matrix_addition();
        case 2
            matrix_subtraction();
        case 3
            matrix_multiplication();
        case 4
            matrix_division();
        case 5
            matrix_inverse();
        case 6
            matrix_determinant();
        case 7
            disp('Exiting the program...');
            return;
        otherwise
            disp('Invalid choice. Please select a valid option.');
            matrix_operations();  % Recursively call the function again
    end
end
