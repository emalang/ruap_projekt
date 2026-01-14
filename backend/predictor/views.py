from django.shortcuts import render
from .forms import MushroomForm
from .azure_client import AzureMLClient

def home(request):
    result = None
    raw_pred = None
    error = None

    if request.method == "POST":
        form = MushroomForm(request.POST)
        if form.is_valid():
            try:
                client = AzureMLClient()
                raw_pred = client.predict(form.to_payload_row())  # "p" ili "e"
                result = "POISONOUS" if raw_pred == "p" else "EDIBLE"
            except Exception as ex:
                error = str(ex)
        else:
            error = "Provjeri unos u formi."
    else:
        form = MushroomForm()

    return render(
        request,
        "predictor/home.html",
        {"form": form, "result": result, "raw_pred": raw_pred, "error": error},
    )
