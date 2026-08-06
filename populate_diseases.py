import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from app.models import DiseaseInfo


diseases = [

    {
        "disease_name": "Tomato_Bacterial_spot",
        "plant_name": "Tomato",
        "symptoms": "Small dark spots on leaves and fruits.",
        "causes": "Bacterial infection.",
        "treatment": "Remove infected parts and apply copper-based bactericide.",
        "prevention": "Use disease-free seeds and avoid overhead watering."
    },

    {
        "disease_name": "Tomato_Early_blight",
        "plant_name": "Tomato",
        "symptoms": "Brown circular spots with concentric rings on older leaves.",
        "causes": "Fungal infection (Alternaria solani).",
        "treatment": "Remove infected leaves and apply fungicide.",
        "prevention": "Rotate crops and avoid excessive moisture."
    },

    {
        "disease_name": "Tomato_Late_blight",
        "plant_name": "Tomato",
        "symptoms": "Large dark brown lesions on leaves and stems.",
        "causes": "Phytophthora infestans fungus-like organism.",
        "treatment": "Remove infected plants and use recommended fungicides.",
        "prevention": "Avoid wet foliage and ensure proper air circulation."
    },

    {
        "disease_name": "Tomato_Leaf_Mold",
        "plant_name": "Tomato",
        "symptoms": "Yellow patches on upper leaf surface with mold underneath.",
        "causes": "Fungal infection.",
        "treatment": "Improve ventilation and apply fungicide.",
        "prevention": "Reduce humidity and avoid overcrowding."
    },

    {
        "disease_name": "Tomato_Septoria_leaf_spot",
        "plant_name": "Tomato",
        "symptoms": "Small circular spots with dark borders.",
        "causes": "Septoria fungus.",
        "treatment": "Remove affected leaves and spray fungicide.",
        "prevention": "Keep leaves dry and rotate crops."
    },

    {
        "disease_name": "Tomato_Spider_mites_Two_spotted_spider_mite",
        "plant_name": "Tomato",
        "symptoms": "Yellow speckles, webbing, and drying leaves.",
        "causes": "Spider mite infestation.",
        "treatment": "Spray miticide or insecticidal soap.",
        "prevention": "Inspect plants regularly and maintain humidity."
    },

    {
        "disease_name": "Tomato__Target_Spot",
        "plant_name": "Tomato",
        "symptoms": "Brown circular spots with yellow halos.",
        "causes": "Fungal infection.",
        "treatment": "Use suitable fungicide and remove infected leaves.",
        "prevention": "Ensure good airflow and avoid leaf wetness."
    },

    {
        "disease_name": "Tomato__Tomato_YellowLeaf__Curl_Virus",
        "plant_name": "Tomato",
        "symptoms": "Leaves curl upward and turn yellow.",
        "causes": "Virus spread by whiteflies.",
        "treatment": "Remove infected plants and control whiteflies.",
        "prevention": "Use resistant varieties and insect control."
    },

    {
        "disease_name": "Tomato__Tomato_mosaic_virus",
        "plant_name": "Tomato",
        "symptoms": "Light and dark green mosaic pattern on leaves.",
        "causes": "Tomato Mosaic Virus.",
        "treatment": "Remove infected plants and disinfect tools.",
        "prevention": "Use certified seeds and avoid tobacco contamination."
    },

    {
        "disease_name": "Tomato_healthy",
        "plant_name": "Tomato",
        "symptoms": "No disease detected.",
        "causes": "Healthy plant.",
        "treatment": "No treatment required.",
        "prevention": "Continue proper watering, nutrition, and regular monitoring."
    },

    {
        "disease_name": "Potato___Early_blight",
        "plant_name": "Potato",
        "symptoms": "Brown spots with concentric rings on older leaves.",
        "causes": "Alternaria solani fungus.",
        "treatment": "Remove infected leaves and apply fungicide.",
        "prevention": "Rotate crops and avoid excessive moisture."
    },

    {
        "disease_name": "Potato___Late_blight",
        "plant_name": "Potato",
        "symptoms": "Dark water-soaked spots that spread quickly.",
        "causes": "Phytophthora infestans.",
        "treatment": "Remove infected plants and use recommended fungicide.",
        "prevention": "Avoid overhead watering and ensure good air circulation."
    },

    {
        "disease_name": "Potato___healthy",
        "plant_name": "Potato",
        "symptoms": "No disease detected.",
        "causes": "Healthy plant.",
        "treatment": "No treatment required.",
        "prevention": "Continue proper watering and regular care."
    },

    {
        "disease_name": "Pepper__bell___Bacterial_spot",
        "plant_name": "Bell Pepper",
        "symptoms": "Small dark spots on leaves and fruits.",
        "causes": "Bacterial infection.",
        "treatment": "Remove infected leaves and apply copper-based bactericide.",
        "prevention": "Use disease-free seeds and avoid overhead watering."
    },

    {
        "disease_name": "Pepper__bell___healthy",
        "plant_name": "Bell Pepper",
        "symptoms": "No disease detected.",
        "causes": "Healthy plant.",
        "treatment": "No treatment required.",
        "prevention": "Continue proper watering and regular monitoring."
    },

    {
        "disease_name": "Aloe_Vera_Leaf_Spot",
        "plant_name": "Aloe Vera",
        "symptoms": "Brown or black spots on leaves.",
        "causes": "Fungal infection caused by excess moisture.",
        "treatment": "Remove infected leaves and apply fungicide.",
        "prevention": "Avoid overwatering and provide good air circulation."
    },

    {
        "disease_name": "Aloe_Vera_Root_Rot",
        "plant_name": "Aloe Vera",
        "symptoms": "Soft roots, yellow leaves, and wilting.",
        "causes": "Overwatering and poor drainage.",
        "treatment": "Trim rotten roots and repot in dry, well-draining soil.",
        "prevention": "Water only when soil is completely dry."
    },

    {
        "disease_name": "Aloe_Vera_Anthracnose",
        "plant_name": "Aloe Vera",
        "symptoms": "Sunken dark lesions on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Remove infected parts and spray fungicide.",
        "prevention": "Keep leaves dry and avoid overcrowding."
    },

    {
        "disease_name": "Ashoka_Leaf_Spot",
        "plant_name": "Ashoka",
        "symptoms": "Brown spots with yellow margins on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Remove infected leaves and apply fungicide.",
        "prevention": "Avoid excess watering and improve airflow."
    },

    {
        "disease_name": "Ashoka_Powdery_Mildew",
        "plant_name": "Ashoka",
        "symptoms": "White powdery coating on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Spray suitable fungicide.",
        "prevention": "Provide sunlight and good ventilation."
    },

    {
        "disease_name": "Ashoka_Root_Rot",
        "plant_name": "Ashoka",
        "symptoms": "Yellow leaves and decaying roots.",
        "causes": "Poor drainage and overwatering.",
        "treatment": "Improve drainage and remove infected roots.",
        "prevention": "Do not allow waterlogging."
    },

    {
        "disease_name": "Banana_Panama_Disease",
        "plant_name": "Banana",
        "symptoms": "Yellowing leaves and plant wilting.",
        "causes": "Fusarium fungus.",
        "treatment": "Remove infected plants.",
        "prevention": "Use disease-resistant varieties and healthy planting material."
    },

    {
        "disease_name": "Banana_Black_Sigatoka",
        "plant_name": "Banana",
        "symptoms": "Dark streaks and black spots on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Apply fungicide and remove infected leaves.",
        "prevention": "Maintain proper spacing and air circulation."
    },

    {
        "disease_name": "Banana_Bunchy_Top_Virus",
        "plant_name": "Banana",
        "symptoms": "Small upright leaves forming a bunch at the top.",
        "causes": "Banana Bunchy Top Virus spread by aphids.",
        "treatment": "Remove infected plants and control aphids.",
        "prevention": "Use virus-free planting material."
    },

    {
        "disease_name": "Banana_Anthracnose",
        "plant_name": "Banana",
        "symptoms": "Dark sunken spots on fruits.",
        "causes": "Fungal infection.",
        "treatment": "Apply fungicide and remove infected fruits.",
        "prevention": "Handle fruits carefully and maintain field hygiene."
    },

    {
        "disease_name": "Banyan_Leaf_Spot",
        "plant_name": "Banyan",
        "symptoms": "Brown or black spots on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Remove infected leaves and apply fungicide.",
        "prevention": "Avoid excess moisture and improve air circulation."
    },

    {
        "disease_name": "Banyan_Powdery_Mildew",
        "plant_name": "Banyan",
        "symptoms": "White powder-like coating on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Apply suitable fungicide.",
        "prevention": "Provide proper sunlight and ventilation."
    },

    {
        "disease_name": "Banyan_Root_Rot",
        "plant_name": "Banyan",
        "symptoms": "Yellowing leaves and rotting roots.",
        "causes": "Overwatering and poor drainage.",
        "treatment": "Improve drainage and remove infected roots.",
        "prevention": "Avoid waterlogging."
    },

    {
        "disease_name": "Coconut_Bud_Rot",
        "plant_name": "Coconut",
        "symptoms": "Rotting of the central growing bud.",
        "causes": "Phytophthora fungal infection.",
        "treatment": "Remove infected tissues and apply recommended fungicide.",
        "prevention": "Maintain proper drainage and field sanitation."
    },

    {
        "disease_name": "Coconut_Stem_Bleeding",
        "plant_name": "Coconut",
        "symptoms": "Dark reddish-brown liquid oozes from the trunk.",
        "causes": "Fungal infection.",
        "treatment": "Remove affected bark and apply fungicide.",
        "prevention": "Avoid trunk injuries and maintain healthy trees."
    },

    {
        "disease_name": "Coconut_Leaf_Blight",
        "plant_name": "Coconut",
        "symptoms": "Yellowing and drying of leaf tips.",
        "causes": "Fungal infection.",
        "treatment": "Remove infected leaves and spray fungicide.",
        "prevention": "Ensure proper nutrition and sanitation."
    },

    {
        "disease_name": "Guava_Anthracnose",
        "plant_name": "Guava",
        "symptoms": "Dark sunken lesions on fruits and leaves.",
        "causes": "Colletotrichum fungal infection.",
        "treatment": "Apply fungicide and remove infected fruits.",
        "prevention": "Maintain orchard hygiene and prune regularly."
    },

    {
        "disease_name": "Guava_Wilt",
        "plant_name": "Guava",
        "symptoms": "Leaves wilt and branches gradually dry.",
        "causes": "Soil-borne fungal pathogens.",
        "treatment": "Remove severely affected plants and improve soil drainage.",
        "prevention": "Use healthy planting material and avoid waterlogging."
    },

    {
        "disease_name": "Guava_Algal_Leaf_Spot",
        "plant_name": "Guava",
        "symptoms": "Orange to reddish circular spots on leaves.",
        "causes": "Algal infection.",
        "treatment": "Spray copper-based fungicide.",
        "prevention": "Improve air circulation and avoid excessive humidity."
    },

    {
        "disease_name": "Turmeric_Leaf_Blotch",
        "plant_name": "Haldi",
        "symptoms": "Brown oval spots with yellow margins on leaves.",
        "causes": "Taphrina fungal infection.",
        "treatment": "Remove infected leaves and spray fungicide.",
        "prevention": "Avoid excessive moisture and maintain field sanitation."
    },

    {
        "disease_name": "Turmeric_Leaf_Spot",
        "plant_name": "Haldi",
        "symptoms": "Small brown spots that enlarge over time.",
        "causes": "Fungal infection.",
        "treatment": "Apply recommended fungicide.",
        "prevention": "Ensure proper spacing and good air circulation."
    },

    {
        "disease_name": "Turmeric_Rhizome_Rot",
        "plant_name": "Haldi",
        "symptoms": "Yellowing leaves and rotting rhizomes.",
        "causes": "Pythium fungal infection.",
        "treatment": "Remove infected plants and improve drainage.",
        "prevention": "Avoid waterlogging and use healthy seed rhizomes."
    },

    {
        "disease_name": "Hibiscus_Leaf_Spot",
        "plant_name": "Hibiscus",
        "symptoms": "Brown or black spots on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Remove infected leaves and spray fungicide.",
        "prevention": "Avoid overhead watering and improve airflow."
    },

    {
        "disease_name": "Hibiscus_Powdery_Mildew",
        "plant_name": "Hibiscus",
        "symptoms": "White powder-like coating on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Apply suitable fungicide.",
        "prevention": "Provide proper sunlight and ventilation."
    },

    {
        "disease_name": "Hibiscus_Root_Rot",
        "plant_name": "Hibiscus",
        "symptoms": "Wilting, yellow leaves, and root decay.",
        "causes": "Overwatering and poor drainage.",
        "treatment": "Trim affected roots and repot in well-drained soil.",
        "prevention": "Avoid overwatering."
    },

    {
        "disease_name": "Lotus_Leaf_Spot",
        "plant_name": "Lotus",
        "symptoms": "Dark brown circular spots on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Remove infected leaves and apply fungicide.",
        "prevention": "Maintain clean pond water and remove dead plant material."
    },

    {
        "disease_name": "Lotus_Root_Rot",
        "plant_name": "Lotus",
        "symptoms": "Soft, decaying roots and poor plant growth.",
        "causes": "Fungal infection in waterlogged conditions.",
        "treatment": "Remove infected roots and improve water quality.",
        "prevention": "Keep pond clean and avoid stagnant water."
    },

    {
        "disease_name": "Lotus_Gray_Mold",
        "plant_name": "Lotus",
        "symptoms": "Gray fuzzy mold on leaves and flowers.",
        "causes": "Botrytis fungal infection.",
        "treatment": "Remove infected parts and apply fungicide.",
        "prevention": "Provide good air circulation and remove dead plant material."
    },

    {
        "disease_name": "Mango_Anthracnose",
        "plant_name": "Mango",
        "symptoms": "Black sunken spots on leaves, flowers, and fruits.",
        "causes": "Colletotrichum fungal infection.",
        "treatment": "Remove infected parts and apply fungicide.",
        "prevention": "Prune regularly and avoid excess moisture."
    },

    {
        "disease_name": "Mango_Powdery_Mildew",
        "plant_name": "Mango",
        "symptoms": "White powdery coating on leaves and flowers.",
        "causes": "Fungal infection.",
        "treatment": "Spray suitable fungicide.",
        "prevention": "Maintain proper spacing and air circulation."
    },

    {
        "disease_name": "Mango_Bacterial_Canker",
        "plant_name": "Mango",
        "symptoms": "Cracks on branches and dark lesions on leaves and fruits.",
        "causes": "Bacterial infection.",
        "treatment": "Prune infected branches and use copper-based bactericide.",
        "prevention": "Use healthy planting material and disinfect pruning tools."
    },

    {
        "disease_name": "Mango_Malformation",
        "plant_name": "Mango",
        "symptoms": "Abnormal growth of flowers and shoots.",
        "causes": "Fungal infection and environmental factors.",
        "treatment": "Remove affected shoots and apply recommended fungicide.",
        "prevention": "Prune regularly and maintain orchard hygiene."
    },

    {
        "disease_name": "Neem_Leaf_Spot",
        "plant_name": "Neem",
        "symptoms": "Small brown or black spots on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Remove infected leaves and spray fungicide.",
        "prevention": "Avoid excessive watering and improve air circulation."
    },

    {
        "disease_name": "Neem_Powdery_Mildew",
        "plant_name": "Neem",
        "symptoms": "White powdery coating on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Apply suitable fungicide.",
        "prevention": "Ensure good sunlight and ventilation."
    },

    {
        "disease_name": "Neem_Root_Rot",
        "plant_name": "Neem",
        "symptoms": "Yellowing leaves, wilting, and root decay.",
        "causes": "Overwatering and soil-borne fungi.",
        "treatment": "Improve drainage and remove infected roots.",
        "prevention": "Avoid waterlogging and use well-drained soil."
    },

    {
        "disease_name": "Papaya_Ring_Spot_Virus",
        "plant_name": "Papaya",
        "symptoms": "Yellow rings on fruits and mosaic patterns on leaves.",
        "causes": "Papaya Ringspot Virus spread by aphids.",
        "treatment": "Remove infected plants and control aphids.",
        "prevention": "Use virus-free seedlings and manage insect vectors."
    },

    {
        "disease_name": "Papaya_Anthracnose",
        "plant_name": "Papaya",
        "symptoms": "Dark sunken spots on fruits and leaves.",
        "causes": "Colletotrichum fungal infection.",
        "treatment": "Apply fungicide and remove infected fruits.",
        "prevention": "Maintain orchard hygiene and avoid fruit injuries."
    },

    {
        "disease_name": "Papaya_Powdery_Mildew",
        "plant_name": "Papaya",
        "symptoms": "White powdery coating on leaves.",
        "causes": "Fungal infection.",
        "treatment": "Spray suitable fungicide.",
        "prevention": "Ensure good air circulation and proper plant spacing."
    },

    {
        "disease_name": "Rose_Black_Spot",
        "plant_name": "Rose",
        "symptoms": "Black circular spots on leaves followed by yellowing.",
        "causes": "Diplocarpon rosae fungus.",
        "treatment": "Remove infected leaves and apply fungicide.",
        "prevention": "Avoid overhead watering and improve airflow."
    },

    {
        "disease_name": "Rose_Powdery_Mildew",
        "plant_name": "Rose",
        "symptoms": "White powdery coating on leaves and buds.",
        "causes": "Fungal infection.",
        "treatment": "Apply suitable fungicide.",
        "prevention": "Provide good sunlight and proper ventilation."
    },

    {
        "disease_name": "Rose_Rust",
        "plant_name": "Rose",
        "symptoms": "Orange or rust-colored pustules on leaf undersides.",
        "causes": "Fungal infection.",
        "treatment": "Remove infected leaves and spray fungicide.",
        "prevention": "Keep foliage dry and maintain good air circulation."
    },

    {
        "disease_name": "Rose_Downy_Mildew",
        "plant_name": "Rose",
        "symptoms": "Purple to dark brown spots with leaf drop.",
        "causes": "Downy mildew pathogen.",
        "treatment": "Apply fungicide and remove infected foliage.",
        "prevention": "Avoid excess humidity and overcrowding."
    },

    {
        "disease_name": "Sunflower_Downy_Mildew",
        "plant_name": "Sunflower",
        "symptoms": "Yellow leaves with white fungal growth underneath.",
        "causes": "Downy mildew pathogen.",
        "treatment": "Remove infected plants and apply fungicide.",
        "prevention": "Use resistant varieties and avoid waterlogging."
    },

    {
        "disease_name": "Sunflower_Rust",
        "plant_name": "Sunflower",
        "symptoms": "Orange-brown pustules on leaves.",
        "causes": "Rust fungus.",
        "treatment": "Spray appropriate fungicide.",
        "prevention": "Rotate crops and remove infected plant debris."
    },

    {
        "disease_name": "Sunflower_Alternaria_Leaf_Spot",
        "plant_name": "Sunflower",
        "symptoms": "Dark brown spots with concentric rings on leaves.",
        "causes": "Alternaria fungal infection.",
        "treatment": "Apply fungicide and remove infected leaves.",
        "prevention": "Maintain field sanitation and proper spacing."
    },







]


for disease in diseases:

    DiseaseInfo.objects.update_or_create(
        disease_name=disease["disease_name"],
        defaults=disease
    )

print("✅ Tomato diseases added successfully!")