function matrix_subtraction()
    disp('Matrix Subtraction');
    A = input('Enter the first matrix: ');
    B = input('Enter the second matrix: ');
    
    if size(A) == size(B)
        C = A - B;
        disp('The result of subtraction is: ');
        disp(C);
    else
        disp('Error: Matrices must be of the same size for subtraction.');
    end
    
    matrix_operations();  % Return to the main menu
end
