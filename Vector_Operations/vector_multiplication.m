function vector_multiplication()
    disp('Element-wise Vector Multiplication');
    v1 = input('Enter the first vector: ');
    v2 = input('Enter the second vector: ');

    if length(v1) == length(v2)
        result = v1 .* v2;  % Element-wise multiplication
        disp('The result of element-wise vector multiplication is: ');
        disp(result);

        % Plot the vectors
        plot_vectors({v1, v2, result}, {'A', 'B', 'C = A .* B'});
    else
        disp('Error: Vectors must be of the same dimension for multiplication.');
    end
    
    vector_operations();  % Return to the main menu
end
