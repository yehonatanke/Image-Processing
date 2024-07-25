function binaryImage = thresholdImage(grayImage, T)
    % קבלת מימדי התמונה
    [rows, cols] = size(grayImage);
    
    % יצירת מטריצה בינארית בגודל התמונה המקורית
    binaryImage = zeros(rows, cols);
    
    % ביצוע thresholding
    for i = 1:rows
        for j = 1:cols
            if grayImage(i,j) <= T
                binaryImage(i,j) = 0;  % black
            else
                binaryImage(i,j) = 255;  % white
            end
        end
    end
    
    % המרה למטריצה לוגית
    binaryImage = logical(binaryImage);
end

% קריאה לפונקציה עם תמונות לדוגמה
cameraman = imread('cameraman.tif');
spine = imread('spine.tif');

% ביצוע thresholding עבור שתי התמונות עם ערכי סף שונים
binaryCameraman = thresholdImage(cameraman, 128);
binarySpine = thresholdImage(spine, 100);

% תוצאות
figure;
subplot(2,2,1); imshow(cameraman); title('Original Cameraman');
subplot(2,2,2); imshow(binaryCameraman); title('Binary Cameraman');
subplot(2,2,3); imshow(spine); title('Original Spine');
subplot(2,2,4); imshow(binarySpine); title('Binary Spine');
