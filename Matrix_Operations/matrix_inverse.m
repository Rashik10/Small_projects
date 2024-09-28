function matrix_inverse()
    disp('Matrix Inverse');
    A = input('Enter the matrix: ');

    if size(A, 1) == size(A, 2) && det(A) ~= 0
        C = inv(A);
        disp('The inverse of the matrix is: ');
        disp(C);
    else
        disp('Error: Inverse requires a square and non-singular matrix.');
    end
    
    matrix_operations();  % Return to the main menu
end
