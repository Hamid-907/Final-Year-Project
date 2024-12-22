<?php
// Check if a file was uploaded
if (isset($_FILES['file'])) {
    // Define the target directory for uploads
    $targetDir = "uploads/";

    // Ensure the 'uploads' directory exists, create if not
    if (!is_dir($targetDir)) {
        mkdir($targetDir, 0755, true);
    }

    // Get the original filename
    $targetFile = $targetDir . basename($_FILES["file"]["name"]);

    // Check for upload errors
    if ($_FILES["file"]["error"] > 0) {
        echo "Error: " . $_FILES["file"]["error"] . "<br />";
    } else {
        // Move the uploaded file to the target directory
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $targetFile)) {
            echo "File uploaded successfully!";
            echo "<br />Saved as: " . $targetFile;
        } else {
            echo "Error: There was a problem uploading your file.";
        }
    }
} else {
    echo "No file was uploaded.";
}
?>
