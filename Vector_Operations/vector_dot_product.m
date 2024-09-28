function vector_dot_product()
    disp('Dot Product');
    v1 = input('Enter the first vector: ');
    v2 = input('Enter the second vector: ');

    if length(v1) == length(v2)
        result = dot(v1, v2);
        disp('The result of the dot product is: ');
        disp(result);
    else
        disp('Error: Vectors must be of the same dimension for the dot product.');
    end
    
    vector_operations();  % Return to the main menu
end
