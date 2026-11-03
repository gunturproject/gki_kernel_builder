# ⚡ Android 16 GKI Kernel (`6.12.30` / `6.12.38`)

### 📲 Flashing Instructions
1. Download **`*-Bundle.zip`** for your root flavor and extract it.
2. Flash **`*-AnyKernel3.zip`** using the **[Kernel Flasher](https://github.com/fatalcoder524/KernelFlasher/releases)** app. *(Vendor module bypass is built-in)*
3. Install the included **matching Root Manager APK** (`*.apk`) for SukiSU-Ultra or KernelSU-Next.
4. Reboot your device.
5. For SukiSU-Ultra only, optionally flash **[susfs4ksu-module (by sidex15)](https://github.com/sidex15/susfs4ksu-module/releases)**. The SukiSU-specific in-tree patch is not applied to KernelSU-Next.
6. *(Optional)* Flash **`Nethunter-Wireless-Modules.zip`** in your Root Manager to enable external WiFi drivers, BadUSB HID gadget support, and the interactive **Material 3 Kernel Manager WebUI** (accessible via the module's WebUI/Action button).
7. *(Optional)* Flash **`NoMount-*.zip`** for VFS mount stealth.

---

### 📜 Commits & Changelog
{{CHANGELOG}}
