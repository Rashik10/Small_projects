function plot_vectors(vectors, labels)
    % vectors: Cell array of vectors to plot
    % labels: Cell array of labels for each vector

    n = length(vectors{1});  % Determine the dimension (2D or 3D)

    if n == 2
        % 2D Plot
        figure;
        hold on;
        for i = 1:length(vectors)
            quiver(0, 0, vectors{i}(1), vectors{i}(2), 0, 'LineWidth', 2);
        end
        legend(labels);
        xlim([-10 10]);
        ylim([-10 10]);
        grid on;
        hold off;
        title('2D Vector Plot');
    elseif n == 3
        % 3D Plot
        figure;
        hold on;
        for i = 1:length(vectors)
            quiver3(0, 0, 0, vectors{i}(1), vectors{i}(2), vectors{i}(3), 0, 'LineWidth', 2);
        end
        legend(labels);
        xlim([-10 10]);
        ylim([-10 10]);
        zlim([-10 10]);
        grid on;
        hold off;
        title('3D Vector Plot');
    else
        disp('Error: Only 2D or 3D vectors can be plotted.');
    end
end
