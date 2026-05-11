import customtkinter as ctk
from tkinter import filedialog
from main import swap

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ACCENT = "#3B82F6"
BG     = "#0F1117"
CARD   = "#1A1D27"
BORDER = "#2A2D3A"
FG     = "#E2E8F0"
MUTED  = "#64748B"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Batch Replace")
        self.geometry("520x680")
        self.resizable(False, False)
        self.configure(fg_color=BG)

        self._build()

    def _build(self):
        # ── Title ────────────────────────────────────────────────
        ctk.CTkLabel(
            self, text="Text Swap",
            font=ctk.CTkFont(family="Courier New", size=22, weight="bold"),
            text_color=FG,
        ).pack(pady=(32, 2))

        ctk.CTkLabel(
            self, text="find & replace text across files in a directory",
            font=ctk.CTkFont(size=12),
            text_color=MUTED,
        ).pack(pady=(0, 24))

        # ── Card ─────────────────────────────────────────────────
        card = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12)
        card.pack(padx=32, fill="x")

        def row(label, row_i, placeholder, is_dir=False):
            ctk.CTkLabel(
                card, text=label,
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=MUTED, anchor="w",
            ).grid(row=row_i*2, column=0, columnspan=2, sticky="w", padx=20, pady=(16, 2))

            entry = ctk.CTkEntry(
                card, placeholder_text=placeholder,
                fg_color=BG, border_color=BORDER, border_width=1,
                text_color=FG, placeholder_text_color=MUTED,
                corner_radius=8, height=36,
                font=ctk.CTkFont(family="Courier New", size=12),
            )
            entry.grid(row=row_i*2+1, column=0, sticky="ew", padx=(20, 4 if is_dir else 20), pady=(0, 0))

            if is_dir:
                btn = ctk.CTkButton(
                    card, text="Browse", width=72, height=36,
                    fg_color=BORDER, hover_color="#3A3D4A",
                    text_color=FG, corner_radius=8,
                    font=ctk.CTkFont(size=12),
                    command=lambda e=entry: self._browse(e),
                )
                btn.grid(row=row_i*2+1, column=1, sticky="e", padx=(0, 20))

            card.grid_columnconfigure(0, weight=1)
            return entry

        self.dir_entry    = row("DIRECTORY",  0, "/path/to/folder",   is_dir=True)
        self.suffix_entry = row("SUFFIX",     1, ".txt")
        self.find_entry   = row("FIND",       2, "old phrase")
        self.replace_entry= row("REPLACE WITH",3,"new phrase")

        # ── Case-insensitive toggle ───────────────────────────────
        self.ci_var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(
            card, text="Case insensitive",
            variable=self.ci_var,
            font=ctk.CTkFont(size=12), text_color=MUTED,
            fg_color=ACCENT, hover_color="#2563EB",
            border_color=BORDER, checkmark_color=FG,
        ).grid(row=9, column=0, columnspan=2, sticky="w", padx=20, pady=(16, 20))

        # ── Run button ────────────────────────────────────────────
        ctk.CTkButton(
            self, text="Run",
            height=42, corner_radius=10,
            fg_color=ACCENT, hover_color="#2563EB",
            font=ctk.CTkFont(family="Courier New", size=14, weight="bold"),
            text_color="#FFFFFF",
            command=self._run,
        ).pack(padx=32, pady=(16, 12), fill="x")

        # ── Status label ──────────────────────────────────────────
        self.status = ctk.CTkLabel(
            self, text="", font=ctk.CTkFont(size=12),
            text_color=MUTED,
        )
        self.status.pack()

    def _browse(self, entry):
        path = filedialog.askdirectory()
        if path:
            entry.delete(0, "end")
            entry.insert(0, path)

    def _run(self):
        directory = self.dir_entry.get().strip()
        suffix    = self.suffix_entry.get().strip()
        find      = self.find_entry.get().strip()
        replace   = self.replace_entry.get().strip()

        if not all([directory, suffix, find]):
            self._set_status("Directory, suffix and find are required.", error=True)
            return

        try:
            changed = swap(directory, suffix, find, replace, self.ci_var.get())
        except Exception as e:
            self._set_status(f"Error: {e}", error=True)
            return

        if not changed:
            self._set_status("No matches found.", error=False)
        else:
            total = sum(changed.values())
            files = len(changed)
            self._set_status(
                f"✓  {total} replacement{'s' if total != 1 else ''} across {files} file{'s' if files != 1 else ''}.",
                error=False,
            )

    def _set_status(self, msg, error=False):
        self.status.configure(
            text=msg,
            text_color="#F87171" if error else "#34D399",
        )


if __name__ == "__main__":
    App().mainloop()