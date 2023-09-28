# Linux Dotfile Repository 🐧💻

Welcome to my Linux Dotfile Repository! Here, you'll find various configuration files and scripts to enhance your Linux experience. Feel free to explore and customize your Linux environment using these dotfiles.

## Configuration Directories 📁

- **zathura** 📚
  - [Description]: Configuration files for Zathura, a highly customizable document viewer (pdf).
  - [Installation]: Copy the contents of the directory and place them in your Zathura configuration folder: ~/.config/zathura/zathurarc

- **terminator** 💻
  - [Description]: Configuration files for Terminator, a terminal emulator.
  - [Installation]: Copy the contents of the directory and place them in your Terminator configuration folder: ~/.config/terminator/config

- **rofi** 🚀
  - [Description]: Configuration files for Rofi, an application launcher and window switcher.
  - [Installation]: Copy the contents of the directory and place them in your Rofi configuration folder: ~/.config/rofi/config.rasi

- **kitty** 🐱
  - [Description]: Configuration files for Kitty, a fast, featureful, and GPU-accelerated terminal emulator.
  - [Installation]: Copy the contents of the directory and place them in your Kitty configuration folder: ~/.config/kitty/kitty.conf

- **htop** 📊
  - [Description]: Configuration files for htop, an interactive system monitor.
  - [Installation]: Copy the contents of the directory and place them in your htop configuration folder: ~/.config/htop/htoprc

- **alacritty** 🔥
  - [Description]: Configuration files for Alacritty, a blazing-fast GPU-accelerated terminal emulator.
  - [Installation]: Copy the contents of the directory and place them in your Alacritty configuration folder: ~/.config/alacritty/alacritty.yml

- **neofetch** 🚀
  - [Description]: Configuration files for Neofetch, a command-line system information tool.
  - [Installation]: Copy the contents of the directory and place them in your Neofetch configuration folder: ~/.config/neofetch/config.conf

- **starship.toml** 🚀
  - [Description]: Configuration file for Starship, a fast and customizable prompt for any shell.
  - [Installation]: Copy the file and place it in: ~/.config/starship.toml

- **ranger** 📂
  - [Description]: Configuration files for Ranger, a console-based file manager.
  - [Installation]: Copy the contents of the directory and place them in your Ranger configuration folder: ~/.config/ranger/rc.conf

## My Own CLI Tool

### English-to-Hebrew Translation Script 🌐

English-to-Hebrew translation without switching the keymap on the keyboard.

*A Python tool - must have python3 installed*

To use, follow these steps:

1. Open your `~/.bashrc` file:

   ```bash
   nano ~/.bashrc
   ```

2. Add the following alias to the end of the file:

    ```bash
    alias us_il="python3 ~/.config/us_to_il/init.py"
    ```

3. Save the file.

Now you can use the tool by executing in the terminal:

```bash
us_il
```

### Enjoy customizing and enhancing your Linux experience with these dotfiles! 🚀🐧💻
