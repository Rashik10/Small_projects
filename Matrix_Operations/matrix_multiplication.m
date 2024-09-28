function matrix_multiplication()
    disp('Matrix Multiplication');
    A = input('Enter the first matrix: ');
    B = input('Enter the second matrix: ');
    
    if size(A, 2) == size(B, 1)
        C = A * B;
        disp('The result of multiplication is: ');
        disp(C);
    else
        disp('Error: Number of columns in the first matrix must be equal to the number of rows in the second matrix.');
    end
    
    matrix_operations();  % Return to the main menu
end
