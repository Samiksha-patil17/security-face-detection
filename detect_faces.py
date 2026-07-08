import boto3
import json

bucket = "security-company-images"
image = "employee.jpg"

s3 = boto3.client("s3")

# Upload image
s3.upload_file(image, bucket, image)

rekognition = boto3.client("rekognition")

response = rekognition.detect_faces(
    Image={
        "S3Object": {
            "Bucket": bucket,
            "Name": image
        }
    },
    Attributes=["DEFAULT"]
)

faces = response["FaceDetails"]

print("Number of Faces:", len(faces))

result = []

for i, face in enumerate(faces, start=1):
    confidence = face["Confidence"]

    print(f"Face {i} Confidence: {confidence}")

    result.append({
        "Face": i,
        "Confidence": confidence
    })

with open("result.json", "w") as f:
    json.dump(result, f, indent=4)

print("result.json created")
