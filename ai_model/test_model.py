import onnxruntime as ort

session = ort.InferenceSession("model.onnx")

print("✅ Model Loaded Successfully!")

print("\nINPUTS")
for i in session.get_inputs():
    print("Name :", i.name)
    print("Shape:", i.shape)
    print("Type :", i.type)

print("\nOUTPUTS")
for o in session.get_outputs():
    print("Name :", o.name)
    print("Shape:", o.shape)
    print("Type :", o.type)