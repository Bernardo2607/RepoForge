import customtkinter as ctk
from pathlib import Path
from tkinter import filedialog
import requests
import json

selected_template = None
selected_folder = None

structures = {
    'Python CLI': [
        'src/',
        'src/__init__.py',
        'src/main.py',
        'tests/',
        'tests/__init__.py',
        '.gitignore',
        'requirements.txt',
        'README.md'
    ],
    'FastAPI': [
        'app/',
        'app/__init__.py',
        'app/routes/',
        'app/models/',
        'app/services',
        'app/database',
        'app/main.py',
        'tests/',
        'tests/__init__.py',
        '.env',
        '.gitignore',
        'requirements.txt',
        'README.md'
    ],
    'React': [
        'src/',
        'src/components/',
        'src/pages',
        'src/hooks',
        'src/assets',
        'src/App.jsx',
        'src/main.jsx',
        'public/',
        'public/index.html',
        '.gitignore',
        'package.json',
        'README.md'
        ],
    'Discord bot': [
        'commands/',
        'events/',
        'utils/',
        '.env',
        '.gitignore',
        'main.py',
        'requirements.txt',
        'README.md'
    ]
}

RepoForge = ctk.CTk()
RepoForge.title('RepoForge')
RepoForge.geometry('400x600')

font1 = ctk.CTkFont(family='Times New Roman', size=12)
font2 = ctk.CTkFont(family='Times New Roman', size=25)

title = ctk.CTkLabel(RepoForge, text='RepoForge', font=font2)
desc = ctk.CTkLabel(RepoForge, text='A new way to create repositories', font=font1)

title.pack(pady=10)
desc.pack()
ctk.set_appearance_mode('dark')

def create_repo():
    global info_label
    name = name_project.get()
    description = desc_project.get()
    files = structures.get(selected_template)
    
    if Path(name).exists():
        info_label.configure(text=f'name {name} alredy exists!', text_color = 'red')
        return
    
    for item in files:
        
        if not selected_folder:
            info_label.configure(text='Please, select a folder first!', text_color='red')
            return

        archive = Path(selected_folder) / name / item

        if item.endswith('/'):
            archive.mkdir(parents=True, exist_ok=True)
        elif item == 'README.md':
            archive.parent.mkdir(parents=True, exist_ok=True)
            archive.write_text(f'##{name}\n\n{description}')
        else:
            archive.parent.mkdir(parents=True, exist_ok=True)
            archive.touch()
    info_label.configure(text=f'Project {name} created successfully!', text_color='#2ecc71', font=font1)


def select_template(template):
    global selected_template
    selected_template = template
    create_button.configure(state='normal', text=f'Create {selected_template} repo', fg_color='green', command=create_repo)

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        global selected_folder
        selected_folder = folder
        global folder_label
        folder_label.configure(text=folder)

def start():
    
    new_project.pack_forget()
    github_checkbox.pack_forget()
    global name_project, desc_project

    name_title = ctk.CTkLabel(RepoForge, text='Project name')
    name_title.pack()

    name_project = ctk.CTkEntry(RepoForge, placeholder_text='insert the name')
    name_project.pack()

    desc_title = ctk.CTkLabel(RepoForge, text='Project description')
    desc_project = ctk.CTkEntry(RepoForge, placeholder_text='insert the description')
    desc_title.pack()
    desc_project.pack()

    templates = [
        'Python CLI',
        'FastAPI',
        'React',
        'Discord bot'
    ]

    tec_title = ctk.CTkLabel(RepoForge, text='Select your tecnology')
    tec_title.pack()

    for i in templates:
       tec = ctk.CTkButton(RepoForge, text=i, command=lambda t=i: select_template(t))
       tec.pack(pady=5)
    
    global folder_label
    folder_label = ctk.CTkLabel(RepoForge, text='No folder selected')
    folder_label.pack()        
    
    folder_button = ctk.CTkButton(RepoForge, text='Choose folder', command=choose_folder)
    folder_button.pack(pady=5)

    global create_button
    create_button = ctk.CTkButton(RepoForge, text='Select a tecnology first', state='disabled')
    create_button.pack(pady=10)
    
    global info_label
    info_label = ctk.CTkLabel(RepoForge, text='', font=font1)
    info_label.pack(pady=5)


new_project = ctk.CTkButton(RepoForge, text='New Project[+]', command=start)
new_project.pack(pady=10)

checkbox_var = ctk.IntVar()
github_checkbox = ctk.CTkCheckBox(RepoForge, text='Also create on GitHub', variable=checkbox_var)
github_checkbox.pack()

RepoForge.mainloop()