�
    �$f-	  �                   �   � d dl Z d dlmZ d dlmZmZmZmZ d dlm	Z
 dZdZd� Zg d�Zd	� Zd
� Z e�   �         Z ee�  �         dS )�    N)�Console)�Progress�	BarColumn�
TextColumn�TimeElapsedColumn)�printz
[thistle1]z[green_yellow]c                  �:  � t           �                    d�  �         t          dt          � dt          � dt          � dt          � dt          � dt          � dt          � d	t          � d
t          � dt          � dt          � dt          � dt          � dt          � d��  �         d S )N�clear� uO   
████████╗██████╗░██╗░░░██╗u   ░░███╗░░
 uN   ╚══██╔══╝██╔══██╗██║░░░██║u   ░████║░░
 uN   ░░░██║░░░██████╦╝╚██╗░██╔╝u   ██╔██║░░
 uK   ░░░██║░░░██╔══██╗░╚████╔╝u   ░╚═╝██║░░
 uH   ░░░██║░░░██████╦╝░░╚██╔╝u    ░░███████╗
 uE   ░░░╚═╝░░░╚═════╝░░░░╚═╝u"   ░░░╚══════╝
z#teleboost module installer version z1.0
)�os�system�rishabh�pk�lg� �    �6/storage/emulated/0/ALLFREESCRIPT/TELEBOOST/install.py�bannerr      s  � ��I�I�g����� �"� � �OQ�� ��� �TV�� � �� � UW�� � �	� � RT�	� �
 �� �
 OQ�� � �� � LN�� � �� � )+�� � � � � � � r   )�telethon�requests�tgcrypto�pyrogram�richzsetuptools==66.0.0�picklec                 ��   � g }t          �   �          | D ]7}	 t          |�  �         �# t          $ r |�                    |�  �         Y �4w xY w|rt	          |�  �         d S t
          �                    d�  �         d S )NzD[bold green]All required modules are already installed.[/bold green])r   �
__import__�ImportError�append�install_modules�consoler   )�modules�not_installed_modules�modules      r   �check_and_install_modulesr$      s�   � ���
�H�H�H�� 1� 1��	1��v������� 	1� 	1� 	1�!�(�(��0�0�0�0�0�	1���� � ^��-�.�.�.�.�.����\�]�]�]�]�]s   �&�A�Ac           	      �  � t           �                    d�  �         t          t          dd��  �        t	          d��  �        ddt          �   �         �  �        5 }|�                    d	t          | �  �        d
��  �        }| D ]M}|�                    |dd|� d���  �         t          j
        dd|dg�  �         |�                    |d��  �         �N	 d d d �  �         n# 1 swxY w Y   t           �                    d�  �         d S )Nz4[bold cyan]Installing missing modules...[/bold cyan]z[cyan]{task.fields[name]}�right)�justify�   )�	bar_widthz-[progress.percentage]{task.percentage:>3.0f}%u   •z[cyan]Installing...�Modules)�total�name�   zInstalling z...)�advance�description�pip�installz--quiet)�	completedz7[bold green]Module installation completed.[/bold green])r    r   r   r   r   r   �add_task�len�update�
subprocess�call)r!   �progress�taskr#   s       r   r   r   #   sO  � ��M�M�H�I�I�I�	��.��@�@�@��B����7�����
� 
� /� 
�� � �!6�c�'�l�l�QZ� �[�[��� 	/� 	/�F��O�O�D�!�9R�v�9R�9R�9R�O�S�S�S��O�U�I�v�y�A�B�B�B��O�O�D�A�O�.�.�.�.�	/�/� /� /� /� /� /� /� /� /� /� /���� /� /� /� /� �M�M�K�L�L�L�L�Ls   �A6C�C�!C)r6   �rich.consoler   �rich.progressr   r   r   r   r   r   r   r   r   r   �required_modulesr$   r   r    r   r   r   �<module>r=      s�   �� � � � �  �  �  �  �  �  � L� L� L� L� L� L� L� L� L� L� L� L� !� !� !� !� !� !�����
� 
� 
� l�k�k� �^� ^� ^�M� M� M�( �'�)�)�� � �*� +� +� +� +� +r   