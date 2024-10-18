% Main Script - CAM-based kNN and k-means with Plots
clear; clc;

% Parameters
mask_bits = 2;  % Number of bits to mask for CAM approximation
k = 2;          % Number of neighbors for kNN
num_clusters = 2; % Number of clusters for k-means
num_samples = 100; % Number of samples for testing

% Generate random 8-bit data samples (binary patterns)
data = randi([0, 255], num_samples, 1);  % Random 8-bit integers
labels = randi([1, num_clusters], num_samples, 1); % Random labels for k-means

% Query for kNN (random binary pattern)
query = randi([0, 255]);

% Perform CAM-based kNN
fprintf('Performing CAM-based kNN...\n');
neighbors = cam_knn(data, query, k, mask_bits);
fprintf('Neighbors found (CAM-based): %d\n', neighbors);

% Perform traditional Euclidean-based kNN for comparison
fprintf('Performing Euclidean-based kNN...\n');
euclidean_neighbors = euclidean_knn(data, query, k);
fprintf('Neighbors found (Euclidean-based): %d\n', euclidean_neighbors);

% Plot the kNN results
figure;
subplot(1, 2, 1);
plot_knn(data, query, neighbors, 'CAM-based kNN');
subplot(1, 2, 2);
plot_knn(data, query, euclidean_neighbors, 'Euclidean-based kNN');

% Perform CAM-based k-means clustering
fprintf('Performing CAM-based k-means...\n');
[cam_clusters, cam_centroids] = cam_kmeans(data, num_clusters, mask_bits);
fprintf('CAM-based k-means cluster assignment:\n');
disp(cam_clusters);

% Perform traditional Euclidean-based k-means for comparison
fprintf('Performing Euclidean-based k-means...\n');
[euclidean_clusters, euclidean_centroids] = kmeans(data, num_clusters);
fprintf('Euclidean-based k-means cluster assignment:\n');
disp(euclidean_clusters);

% Plot the k-means clustering results
figure;
subplot(1, 2, 1);
plot_clusters(data, cam_clusters, cam_centroids, 'CAM-based k-means');
subplot(1, 2, 2);
plot_clusters(data, euclidean_clusters, euclidean_centroids, 'Euclidean-based k-means');


%% CAM-based kNN function
function neighbors = cam_knn(data, query, k, mask_bits)
    distances = cam_approx_distance(data, query, mask_bits);
    [~, sorted_indices] = sort(distances);
    neighbors = sorted_indices(1:k);
end

%% Euclidean-based kNN function (for comparison)
function neighbors = euclidean_knn(data, query, k)
    distances = sqrt(sum((data - query).^2, 2));
    [~, sorted_indices] = sort(distances);
    neighbors = sorted_indices(1:k);
end

%% CAM-based k-means function
function [clusters, centroids] = cam_kmeans(data, num_clusters, mask_bits)
    centroids = randi([0, 255], num_clusters, 1);
    clusters = zeros(size(data));

    for iter = 1:100
        prev_centroids = centroids;

        for i = 1:length(data)
            distances = cam_approx_distance(centroids, data(i), mask_bits);
            [~, closest_centroid] = min(distances);
            clusters(i) = closest_centroid;
        end

        for j = 1:num_clusters
            cluster_members = data(clusters == j);
            if ~isempty(cluster_members)
                centroids(j) = round(mean(cluster_members));
            end
        end

        if isequal(prev_centroids, centroids)
            break;
        end
    end
end

%% CAM-based distance approximation function
function distances = cam_approx_distance(data, query, mask_bits)
    distances = zeros(size(data, 1), 1);
    query_binary = dec2bin(query, 8);
    
    for i = 1:length(data)
        data_binary = dec2bin(data(i), 8);
        diff = sum(query_binary ~= data_binary);
        if diff <= mask_bits
            distances(i) = diff;
        else
            distances(i) = inf;
        end
    end
end

%% Plotting kNN results
function plot_knn(data, query, neighbors, title_text)
    scatter(data, zeros(size(data)), 'b', 'filled');
    hold on;
    scatter(query, 0, 'r', 'filled', 'DisplayName', 'Query');
    scatter(data(neighbors), zeros(size(neighbors)), 'g', 'filled', 'DisplayName', 'Neighbors');
    title(title_text);
    xlabel('Data (8-bit values)');
    legend('Data Points', 'Query', 'Neighbors');
    hold off;
end

%% Plotting k-means clustering results
function plot_clusters(data, clusters, centroids, title_text)
    scatter(data, zeros(size(data)), 50, clusters, 'filled');
    hold on;
    scatter(centroids, zeros(size(centroids)), 100, 'r', 'filled', 'DisplayName', 'Centroids');
    title(title_text);
    xlabel('Data (8-bit values)');
    legend('Cluster Data', 'Centroids');
    hold off;
end
