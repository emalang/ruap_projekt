from django import forms

UNKNOWN = "unknown"

# ---- Choice mape (human friendly) ----
ODOR = [
    ("a", "almond"),
    ("l", "anise"),
    ("c", "creosote"),
    ("y", "fishy"),
    ("f", "foul"),
    ("m", "musty"),
    ("n", "none"),
    ("p", "pungent"),
    ("s", "spicy"),
]

CAP_COLOR = [
    ("n", "brown"),
    ("b", "buff"),
    ("c", "cinnamon"),
    ("g", "gray"),
    ("r", "green"),
    ("p", "pink"),
    ("u", "purple"),
    ("e", "red"),
    ("w", "white"),
    ("y", "yellow"),
]

GILL_SIZE = [
    ("b", "broad"),
    ("n", "narrow"),
]

GILL_COLOR = [
    ("k", "black"),
    ("n", "brown"),
    ("b", "buff"),
    ("h", "chocolate"),
    ("g", "gray"),
    ("r", "green"),
    ("o", "orange"),
    ("p", "pink"),
    ("u", "purple"),
    ("e", "red"),
    ("w", "white"),
    ("y", "yellow"),
]

SPORE_PRINT_COLOR = [
    ("k", "black"),
    ("n", "brown"),
    ("b", "buff"),
    ("h", "chocolate"),
    ("r", "green"),
    ("o", "orange"),
    ("u", "purple"),
    ("w", "white"),
    ("y", "yellow"),
]

BRUISES = [
    ("t", "yes"),
    ("f", "no"),
]

RING_TYPE = [
    ("c", "cobwebby"),
    ("e", "evanescent"),
    ("f", "flaring"),
    ("l", "large"),
    ("n", "none"),
    ("p", "pendant"),
    ("s", "sheathing"),
    ("z", "zone"),
]

STALK_ROOT = [
    ("b", "bulbous"),
    ("c", "club"),
    ("u", "cup"),
    ("e", "equal"),
    ("z", "rhizomorphs"),
    ("r", "rooted"),
    ("?", "unknown in data"),
    (UNKNOWN, "not specified"),
]


# ---- SVI FEATUREI koje model očekuje (22) ----
ALL_FEATURES = [
    "cap-shape",
    "cap-surface",
    "cap-color",
    "bruises",
    "odor",
    "gill-attachment",
    "gill-spacing",
    "gill-size",
    "gill-color",
    "stalk-shape",
    "stalk-root",
    "stalk-surface-above-ring",
    "stalk-surface-below-ring",
    "stalk-color-above-ring",
    "stalk-color-below-ring",
    "veil-type",
    "veil-color",
    "ring-number",
    "ring-type",
    "spore-print-color",
    "population",
    "habitat",
]

# ---- 8 prikazanih korisniku ----
VISIBLE_FEATURES = [
    "odor",
    "spore-print-color",
    "gill-color",
    "cap-color",
    "gill-size",
    "bruises",
    "ring-type",
    "stalk-root",
]


class MushroomForm(forms.Form):
    # VISIBLE (8)
    odor = forms.ChoiceField(label="Odor", choices=ODOR)
    spore_print_color = forms.ChoiceField(label="Spore print color", choices=SPORE_PRINT_COLOR)
    gill_color = forms.ChoiceField(label="Gill color", choices=GILL_COLOR)
    cap_color = forms.ChoiceField(label="Cap color", choices=CAP_COLOR)
    gill_size = forms.ChoiceField(label="Gill size", choices=GILL_SIZE)
    bruises = forms.ChoiceField(label="Bruises?", choices=BRUISES)
    ring_type = forms.ChoiceField(label="Ring type", choices=RING_TYPE)
    stalk_root = forms.ChoiceField(label="Stalk root", choices=STALK_ROOT)

    # HIDDEN (ostalih 14) — stalno "unknown"
    cap_shape = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    cap_surface = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    gill_attachment = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    gill_spacing = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    stalk_shape = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    stalk_surface_above_ring = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    stalk_surface_below_ring = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    stalk_color_above_ring = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    stalk_color_below_ring = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    veil_type = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    veil_color = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    ring_number = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    population = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())
    habitat = forms.CharField(initial=UNKNOWN, widget=forms.HiddenInput())

    def to_payload_row(self):
        """
        Vraća dict s TOČNIM imenima stupaca iz dataseta.
        Za neunesene feature-e šaljemo 'unknown' (model ih ignorira zbog handle_unknown='ignore').
        """
        return {
            "cap-shape": self.cleaned_data["cap_shape"],
            "cap-surface": self.cleaned_data["cap_surface"],
            "cap-color": self.cleaned_data["cap_color"],
            "bruises": self.cleaned_data["bruises"],
            "odor": self.cleaned_data["odor"],
            "gill-attachment": self.cleaned_data["gill_attachment"],
            "gill-spacing": self.cleaned_data["gill_spacing"],
            "gill-size": self.cleaned_data["gill_size"],
            "gill-color": self.cleaned_data["gill_color"],
            "stalk-shape": self.cleaned_data["stalk_shape"],
            "stalk-root": self.cleaned_data["stalk_root"],
            "stalk-surface-above-ring": self.cleaned_data["stalk_surface_above_ring"],
            "stalk-surface-below-ring": self.cleaned_data["stalk_surface_below_ring"],
            "stalk-color-above-ring": self.cleaned_data["stalk_color_above_ring"],
            "stalk-color-below-ring": self.cleaned_data["stalk_color_below_ring"],
            "veil-type": self.cleaned_data["veil_type"],
            "veil-color": self.cleaned_data["veil_color"],
            "ring-number": self.cleaned_data["ring_number"],
            "ring-type": self.cleaned_data["ring_type"],
            "spore-print-color": self.cleaned_data["spore_print_color"],
            "population": self.cleaned_data["population"],
            "habitat": self.cleaned_data["habitat"],
        }
