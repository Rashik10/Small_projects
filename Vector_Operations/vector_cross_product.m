function vector_cross_product()
    disp('Cross Product (3D Vectors only)');
    v1 = input('Enter the first 3D vector: ');
    v2 = input('Enter the second 3D vector: ');

    if length(v1) == 3 && length(v2) == 3
        result = cross(v1, v2);
        disp('The result of the cross product is: ');
        disp(result);

        % Plot the vectors
        plot_vectors({v1, v2, result}, {'A', 'B', 'C = A × B'});
    else
        disp('Error: Cross product requires two 3D vectors.');
    end
    
    vector_operations();  % Return to the main menu
end
