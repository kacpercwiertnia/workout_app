from django.db import migrations

def load_initial_data(apps, schema_editor):

    equipments_model = apps.get_model('api', 'Equipments')

    equipments_model.objects.create (
        equipment_name = "Agility ladder"
        )
    equipments_model.objects.create (
        equipment_name = "Barbell"
        )
    equipments_model.objects.create (
        equipment_name = "Battle ropes"
        )
    equipments_model.objects.create (
        equipment_name = "Bench press"
        )        
    equipments_model.objects.create (
        equipment_name = "Bosu ball"
        )
    equipments_model.objects.create (
        equipment_name = "Cable crossover machine"
        )
    equipments_model.objects.create (
        equipment_name = "Cable machine"
        )
    equipments_model.objects.create (
        equipment_name = "Calf raise machine"
        )
    equipments_model.objects.create (
        equipment_name = "Dumbbell"
        )
    equipments_model.objects.create (
        equipment_name = "Elliptical trainer"
        )
    equipments_model.objects.create (
        equipment_name = "Foam roller"
        )
    equipments_model.objects.create (
        equipment_name = "Gymnastic rings"
        )
    equipments_model.objects.create (
        equipment_name = "Jump rope"
        )
    equipments_model.objects.create (
        equipment_name = "Kettlebell"
        )
    equipments_model.objects.create (
        equipment_name = "Lat pulldown machine"
        )
    equipments_model.objects.create (
        equipment_name = "Leg press"
        )
    equipments_model.objects.create (
        equipment_name = "Leg curl machine"
        )
    equipments_model.objects.create (
        equipment_name = "Leg extension machine"
        )
    equipments_model.objects.create (
        equipment_name = "Lifting straps"
        )
    equipments_model.objects.create (
        equipment_name = "Medicine ball"
        )
    equipments_model.objects.create (
        equipment_name = "Plyometric box"
        )
    equipments_model.objects.create (
        equipment_name = "Pull-up bar"
        )
    equipments_model.objects.create (
        equipment_name = "Resistance bands"
        )
    equipments_model.objects.create (
        equipment_name = "Rowing machine"
        )
    equipments_model.objects.create (
        equipment_name = "Squat rack"
        )
    equipments_model.objects.create (
        equipment_name = "Stair climber"
        )
    equipments_model.objects.create (
        equipment_name = "Stationary bike"
        )
    equipments_model.objects.create (
        equipment_name = "TRX suspension trainer"
        )
    equipments_model.objects.create (
        equipment_name = "Treadmill"
        )
    equipments_model.objects.create (
        equipment_name = "Weighted vest"
        )
    equipments_model.objects.create (
        equipment_name = "Weightlifting belt"
        )
    equipments_model.objects.create (
        equipment_name = "Wrist wraps"
        )
    equipments_model.objects.create (
        equipment_name = "Yoga mat"
        )

    muscles_model = apps.get_model('api', 'Muscles')

    muscles_model.objects.create (
        muscle_name = "Chest"
        )
    muscles_model.objects.create (
        muscle_name = "Back"
        )
    muscles_model.objects.create (
        muscle_name = "Shoulders"
        )
    muscles_model.objects.create (
        muscle_name = "Legs"
        )        
    muscles_model.objects.create (
        muscle_name = "Arms"
        )
    muscles_model.objects.create (
        muscle_name = "Abs"
        )
    muscles_model.objects.create (
        muscle_name = "Glutes"
        )
    muscles_model.objects.create (
        muscle_name = "Calves"
        )
    muscles_model.objects.create (
        muscle_name = "Traps"
        )
    muscles_model.objects.create (
        muscle_name = "Forearms"
        )
    muscles_model.objects.create (
        muscle_name = "Full body"
        )
    muscles_model.objects.create (
        muscle_name = "Biceps"
        )
    muscles_model.objects.create (
        muscle_name = "Triceps"
        )

    exercises_model = apps.get_model('api', 'Exercises')

    exercises_model.objects.create (
        exercise_name = "Bench press",
        muscle_id = muscles_model.objects.get(muscle_name="Chest"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Lie on a bench with a weighted barbell and push it away from your chest."
        )

    exercises_model.objects.create (
        exercise_name = "Squat",
        muscle_id = muscles_model.objects.get(muscle_name="Legs"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Stand with a weighted barbell on your shoulders and squat down and stand up."
        )
    
    exercises_model.objects.create (
        exercise_name = "Deadlift",
        muscle_id = muscles_model.objects.get(muscle_name="Back"),
        difficulty = 'A',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Lift a weighted barbell from the ground to a standing position."
        )

    exercises_model.objects.create (
        exercise_name = "Pull-up",
        muscle_id = muscles_model.objects.get(muscle_name="Back"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Pull-up bar"),
        description = "Hang from a bar and pull your body up until your chin is above the bar."
        )
    
    exercises_model.objects.create (
        exercise_name = "Dumbbell Bicep Curl",
        muscle_id = muscles_model.objects.get(muscle_name="Biceps"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Dumbbell"),
        description = "Hold a dumbbell in each hand and curl them towards your shoulders."
        )

    exercises_model.objects.create (
        exercise_name = "Tricep Pushdown",
        muscle_id = muscles_model.objects.get(muscle_name="Triceps"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Cable machine"),
        description = "Stand facing a cable machine and push down the bar with your hands."
        )
    
    exercises_model.objects.create (
        exercise_name = "Cable Fly",
        muscle_id = muscles_model.objects.get(muscle_name="Chest"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Cable machine"),
        description = "Stand in the middle of a cable machine and pull the cables towards your chest."
        )
    
    exercises_model.objects.create (
        exercise_name = "Leg Press",
        muscle_id = muscles_model.objects.get(muscle_name="Legs"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Leg press"),
        description = "Sit in a leg press machine and push the platform away with your legs."
        )
    
    exercises_model.objects.create (
        exercise_name = "Shoulder Press",
        muscle_id = muscles_model.objects.get(muscle_name="Shoulders"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Stand with a weighted barbell on your shoulders and press it above your head."
        )

    exercises_model.objects.create (
        exercise_name = "Incline Bench Press",
        muscle_id = muscles_model.objects.get(muscle_name="Chest"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Lie on an inclined bench with a weighted barbell and push it away from your chest."
        )

    exercises_model.objects.create (
        exercise_name = "Barbell Row",
        muscle_id = muscles_model.objects.get(muscle_name="Back"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Bend over with a weighted barbell and pull it towards your chest."
        )
    
    exercises_model.objects.create (
        exercise_name = "Seated Cable Row",
        muscle_id = muscles_model.objects.get(muscle_name="Back"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Cable machine"),
        description = "Sit in front of a cable machine and pull the cables towards your chest."
        )

    exercises_model.objects.create (
        exercise_name = "Calf Raise",
        muscle_id = muscles_model.objects.get(muscle_name="Calves"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Calf raise machine"),
        description = "Stand on a calf raise machine and lift your heels as high as possible."
        )

    exercises_model.objects.create (
        exercise_name = "Hammer Curl",
        muscle_id = muscles_model.objects.get(muscle_name="Biceps"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Dumbbell"),
        description = "Hold a dumbbell in each hand and curl them towards your shoulders with your palms facing inwards."
        )

    exercises_model.objects.create (
        exercise_name = "Skull Crusher",
        muscle_id = muscles_model.objects.get(muscle_name="Triceps"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Lie on a bench with a weighted barbell and extend your arms above your head."
        )

    exercises_model.objects.create (
        exercise_name = "Lateral Raise",
        muscle_id = muscles_model.objects.get(muscle_name="Shoulders"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Dumbbell"),
        description = "Hold a dumbbell in each hand and raise them out to your sides until they are at shoulder level."
        )

    exercises_model.objects.create (
        exercise_name = "Reverse Fly",
        muscle_id = muscles_model.objects.get(muscle_name="Back"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Dumbbell"),
        description = "Bend over and hold a dumbbell in each hand, then raise them out to your sides until they are at shoulder level."
        )
    
    exercises_model.objects.create (
        exercise_name = "Leg Extension",
        muscle_id = muscles_model.objects.get(muscle_name="Legs"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Leg extension machine"),
        description = "Sit in a leg extension machine and lift the weights with your legs."
        )

    exercises_model.objects.create (
        exercise_name = "Chest Fly",
        muscle_id = muscles_model.objects.get(muscle_name="Chest"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Dumbbell"),
        description = "Lie on a bench with a dumbbell in each hand and bring them together over your chest."
        )
    
    exercises_model.objects.create (
        exercise_name = "Romanian Deadlift",
        muscle_id = muscles_model.objects.get(muscle_name="Back"),
        difficulty = 'A',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Stand with a weighted barbell and lower it to your shins, then stand back up."
        )
    
    exercises_model.objects.create (
        exercise_name = "Bent Over Row",
        muscle_id = muscles_model.objects.get(muscle_name="Back"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Bend over with a weighted barbell and pull it towards your chest."
        )

    exercises_model.objects.create (
        exercise_name = "Incline Dumbbell Press",
        muscle_id = muscles_model.objects.get(muscle_name="Chest"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Dumbbell"),
        description = "Lie on an inclined bench with a dumbbell in each hand and push them away from your chest."
        )

    exercises_model.objects.create (
        exercise_name = "Front Squat",
        muscle_id = muscles_model.objects.get(muscle_name="Legs"),
        difficulty = 'A',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Stand with a weighted barbell in front of your shoulders and squat down and stand up."
        )

    exercises_model.objects.create (
        exercise_name = "Seated Leg Curl",
        muscle_id = muscles_model.objects.get(muscle_name="Legs"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Leg curl machine"),
        description = "Sit in a leg curl machine and curl the weights with your legs."
        )

    exercises_model.objects.create (
        exercise_name = "Military Press",
        muscle_id = muscles_model.objects.get(muscle_name="Shoulders"),
        difficulty = 'A',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Stand with a weighted barbell on your shoulders and press it above your head with a strict form."
        )

    exercises_model.objects.create (
        exercise_name = "Standing Calf Raise",
        muscle_id = muscles_model.objects.get(muscle_name="Calves"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Calf raise machine"),
        description = "Stand on the edge of a platform and lift your heels as high as possible with your legs straight."
        )

    exercises_model.objects.create (
        exercise_name = "EZ Bar Curl",
        muscle_id = muscles_model.objects.get(muscle_name="Biceps"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Pull-up bar"),
        description = "Hold an EZ bar with an underhand grip and curl it towards your shoulders."
        )

    exercises_model.objects.create (
        exercise_name = "Overhead Tricep Extension",
        muscle_id = muscles_model.objects.get(muscle_name="Triceps"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Dumbbell"),
        description = "Stand with a dumbbell in both hands and extend it above your head with your elbows pointing forward."
        )

    exercises_model.objects.create (
        exercise_name = "Dumbbell Lateral Raise",
        muscle_id = muscles_model.objects.get(muscle_name="Shoulders"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Dumbbell"),
        description = "Hold a dumbbell in each hand and raise them out to your sides until they are at shoulder level."
        )

    exercises_model.objects.create (
        exercise_name = "Leg Curl",
        muscle_id = muscles_model.objects.get(muscle_name="Legs"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Leg curl machine"),
        description = "Lie face down on a leg curl machine and curl the weights towards your glutes."
        )

    exercises_model.objects.create (
        exercise_name = "Standing Calf Raise",
        muscle_id = muscles_model.objects.get(muscle_name="Calves"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Dumbbell"),
        description = "Hold a dumbbell in each hand and raise your heels as high as possible while standing."
        )

    exercises_model.objects.create (
        exercise_name = "Lat Pulldown",
        muscle_id = muscles_model.objects.get(muscle_name="Back"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Lat pulldown machine"),
        description = "Sit in a lat pulldown machine and pull the bar down towards your chest."
        )

    exercises_model.objects.create (
        exercise_name = "Seated Leg Curl",
        muscle_id = muscles_model.objects.get(muscle_name="Legs"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Leg curl machine"),
        description = "Sit in a leg curl machine and curl the weights towards your glutes."
        )

    exercises_model.objects.create (
        exercise_name = "Incline Dumbbell Press",
        muscle_id = muscles_model.objects.get(muscle_name="Chest"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Dumbbell"),
        description = "Lie on an inclined bench with a dumbbell in each hand and push them away from your chest."
        )

    exercises_model.objects.create (
        exercise_name = "Dumbbell Fly",
        muscle_id = muscles_model.objects.get(muscle_name="Chest"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Leg curl machine"),
        description = "Lie on a bench with a dumbbell in each hand and bring them together over your chest."
        )

    exercises_model.objects.create (
        exercise_name = "Standing Military Press",
        muscle_id = muscles_model.objects.get(muscle_name="Shoulders"),
        difficulty = 'A',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Stand with a weighted barbell on your shoulders and press it above your head while standing."
        )

    exercises_model.objects.create (
        exercise_name = "Seated Dumbbell Press",
        muscle_id = muscles_model.objects.get(muscle_name="Shoulders"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Sit on a bench with a dumbbell in each hand and press them above your head."
        )

    exercises_model.objects.create (
        exercise_name = "Barbell Curl",
        muscle_id = muscles_model.objects.get(muscle_name="Biceps"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Hold a weighted barbell with an underhand grip and curl it towards your shoulders."
        )

    exercises_model.objects.create (
        exercise_name = "Close Grip Bench Press",
        muscle_id = muscles_model.objects.get(muscle_name="Triceps"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "Lie on a bench with a weighted barbell and push it away from your chest with a close grip."
        )

    exercises_model.objects.create (
        exercise_name = "Bulgarian Split Squat",
        muscle_id = muscles_model.objects.get(muscle_name="Legs"),
        difficulty = 'A',
        equipment_id = equipments_model.objects.get(equipment_name="Leg curl machine"),
        description = "This is an advanced leg exercise that requires a dumbbell. It involves standing with one leg in front of the other and lowering the back knee towards the ground while keeping the front foot flat on the floor."
        )

    exercises_model.objects.create (
        exercise_name = "Barbell Hip Thrust",
        muscle_id = muscles_model.objects.get(muscle_name="Glutes"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Barbell"),
        description = "This is an intermediate glute exercise that involves using a barbell to lift your hips off the ground. It is done by placing your upper back on a bench, with your feet flat on the floor and the barbell resting across your hips."
        )

    exercises_model.objects.create (
        exercise_name = "Cable Pull-through",
        muscle_id = muscles_model.objects.get(muscle_name="Glutes"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Cable machine"),
        description = "This intermediate glute exercise requires a cable machine. It involves standing facing away from the machine with the cable between your legs, then pulling it through your legs while squeezing your glutes."
        )

    exercises_model.objects.create (
        exercise_name = "Lateral Raises",
        muscle_id = muscles_model.objects.get(muscle_name="Shoulders"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Leg curl machine"),
        description = "This is a beginner shoulder exercise that requires dumbbells. It involves lifting the dumbbells out to the sides of your body until they reach shoulder height."
        )

    exercises_model.objects.create (
        exercise_name = "Incline Dumbbell Press",
        muscle_id = muscles_model.objects.get(muscle_name="Chest"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Leg curl machine"),
        description = "This is an intermediate chest exercise that requires dumbbells and an incline bench. It involves lying on the bench with your feet flat on the floor and pressing the dumbbells up towards the ceiling."
        )

    exercises_model.objects.create (
        exercise_name = "Hanging Leg Raise",
        muscle_id = muscles_model.objects.get(muscle_name="Abs"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Pull-up bar"),
        description = "This intermediate abs exercise requires a pull-up bar. It involves hanging from the bar with your arms straight and lifting your legs up towards your chest."
        )

    exercises_model.objects.create (
        exercise_name = "Farmer’s Walk",
        muscle_id = muscles_model.objects.get(muscle_name="Abs"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Leg curl machine"),
        description = "This is an intermediate full body exercise that requires dumbbells. It involves holding a dumbbell in each hand and walking with good posture, engaging your core and keeping your shoulders back."
        )

    exercises_model.objects.create (
        exercise_name = "Chest Fly",
        muscle_id = muscles_model.objects.get(muscle_name="Chest"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Leg curl machine"),
        description = "This is an intermediate chest exercise that requires a cable machine. It involves standing with one foot in front of the other and pulling the cable handles towards the center of your body."
        )

    exercises_model.objects.create (
        exercise_name = "Jump Rope",
        muscle_id = muscles_model.objects.get(muscle_name="Full body"),
        difficulty = 'B',
        equipment_id = equipments_model.objects.get(equipment_name="Jump rope"),
        description = "This is a beginner full body cardio exercise that requires a jump rope. It involves jumping over the rope as it swings under your feet."
        )

    exercises_model.objects.create (
        exercise_name = "Battle Ropes",
        muscle_id = muscles_model.objects.get(muscle_name="Full body"),
        difficulty = 'I',
        equipment_id = equipments_model.objects.get(equipment_name="Battle ropes"),
        description = "This is an intermediate full body cardio exercise that requires battle ropes. It involves standing with your feet shoulder-width apart and swinging the ropes up and down in alternating patterns."
        )

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
       migrations.RunPython(load_initial_data),
    ]

