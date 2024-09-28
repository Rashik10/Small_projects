function matrix_determinant()
    disp('Matrix Determinant');
    A = input('Enter the matrix: ');

    if size(A, 1) == size(A, 2)
        d = det(A);
        disp('The determinant of the matrix is: ');
        disp(d);
    else
        disp('Error: Determinant requires a square matrix.');
    end
    
    matrix_operations();  % Return to the main menu
end
