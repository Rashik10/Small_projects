function matrix_division()
    disp('Matrix Division (A/B interpreted as A * inv(B))');
    A = input('Enter the first matrix (A): ');
    B = input('Enter the second matrix (B): ');

    if size(B, 1) == size(B, 2) && det(B) ~= 0
        C = A / B;  % Equivalent to A * inv(B)
        disp('The result of division is: ');
        disp(C);
    else
        disp('Error: Division requires a square and non-singular matrix B.');
    end
    
    matrix_operations();  % Return to the main menu
end
