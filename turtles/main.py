import hirstPainting.hirstPainting

turtle_projects = {
    'Hirst Painting':
        'This project generates a dot painting based on colors extracted from an image using the colorgram library.'
}

print('What would you like to do with your turtle today? \n')

# Display menu options
for index, (project_name, project_description) in enumerate(turtle_projects.items(), start=1):
    print(f'{index}. {project_name} - {project_description}')

while True:
    try:
        choice = int(input('\nPlease enter the number corresponding to your choice: '))
        if 1 <= choice <= len(turtle_projects):
            break
        else:
            print('Invalid choice. Please enter a number from the list.')
    except ValueError:
        print('Invalid input. Please enter a number.')

selected_project = list(turtle_projects.keys())[choice - 1]
print(f'You have selected "{selected_project}". Let\'s get started!')

if selected_project == "Hirst Painting":
    hirstPainting.hirstPainting.main()
