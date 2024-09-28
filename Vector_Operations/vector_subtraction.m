function vector_subtraction()
    disp('Vector Subtraction');
    v1 = input('Enter the first vector: ');
    v2 = input('Enter the second vector: ');

    if length(v1) == length(v2)
        result = v1 - v2;
        disp('The result of vector subtraction is: ');
        disp(result);

        % Plot the vectors
        plot_vectors({v1, v2, result}, {'A', 'B', 'C = A - B'});
    else
        disp('Error: Vectors must be of the same dimension for subtraction.');
    end
    
    vector_operations();  % Return to the main menu
end
