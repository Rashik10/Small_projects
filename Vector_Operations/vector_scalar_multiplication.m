function vector_scalar_multiplication()
    disp('Scalar Multiplication');
    v = input('Enter the vector: ');
    s = input('Enter the scalar: ');

    result = s * v;
    disp('The result of scalar multiplication is: ');
    disp(result);

    % Plot the vectors
    plot_vectors({v, result}, {'A', 'B = s * A'});
    
    vector_operations();  % Return to the main menu
end
