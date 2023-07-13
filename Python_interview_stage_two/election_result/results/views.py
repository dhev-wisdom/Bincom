from django.shortcuts import render
from django.db.models import Sum
from .models import PollingUnit, AnnouncedPuResults, AnnouncedLgaResults
from django.shortcuts import render, redirect
from .forms import PollingUnitResultForm
from datetime import datetime
from django.contrib import messages


def home(request):
    return render(request, 'results/base.html')


def polling_unit_result(request, polling_unit_id):
    polling_units = PollingUnit.objects.filter(polling_unit_id=polling_unit_id)

    if not polling_units.exists():
        return render(request, 'results/error.html', {'message': 'Polling Unit not found'})

    uniqueids = polling_units.values_list('uniqueid', flat=True)
    announced_results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid__in=uniqueids)

    context = {
        'polling_units': polling_units,
        'announced_results': announced_results,
    }
    return render(request, 'results/polling_unit_result.html', context)


def lga_results(request):
    if request.method == 'POST':
        selected_lga = request.POST.get('lga')
        party_results = AnnouncedLgaResults.objects.filter(lga_name=selected_lga) \
            .values('party_abbreviation') \
            .annotate(total_score=Sum('party_score'))

        context = {
            'selected_lga': selected_lga,
            'party_results': party_results
        }

        return render(request, 'results/lga_results.html', context)

    # Fetch all unique local government names
    lgas = AnnouncedLgaResults.objects.values_list('lga_name', flat=True).distinct()

    context = {
        'lgas': lgas
    }

    return render(request, 'results/select_lga.html', context)


def add_polling_unit_result(request):
    if request.method == 'POST':
        form = PollingUnitResultForm(request.POST)
        if form.is_valid():
            polling_unit = form.cleaned_data['polling_unit']
            party_results = form.cleaned_data['party_results']

            results_list = party_results.split('\n')
            for result in results_list:
                try:
                    party_abbreviation, party_score = result.strip().split(':')
                    result_obj = AnnouncedPuResults(
                        polling_unit_uniqueid=polling_unit.polling_unit_id,
                        party_abbreviation=party_abbreviation,
                        party_score=int(party_score),
                        entered_by_user=request.user.username,
                        date_entered=datetime.now(),
                        user_ip_address=request.META['REMOTE_ADDR']
                    )
                    result_obj.save()
                except ValueError:
                    messages.error(request, f"Invalid data format: {result}. Please enter party results in the format 'Party Abbreviation:Party Score'.")
                    return redirect('add_polling_unit_result')

            return redirect('polling_unit_results')
    else:
        form = PollingUnitResultForm()

    polling_units = PollingUnit.objects.all()

    context = {
        'form': form,
        'polling_units': polling_units,
    }

    return render(request, 'results/add_polling_unit_result.html', context)


def polling_unit_results(request):
    if request.method == 'POST':
        form = PollingUnitResultForm(request.POST)
        if form.is_valid():
            polling_unit = form.cleaned_data['polling_unit']
            party_results = form.cleaned_data['party_results']

            results_list = party_results.split('\n')
            for result in results_list:
                try:
                    party_abbreviation, party_score = result.strip().split(':')
                    result_obj = AnnouncedPuResults(
                        polling_unit_uniqueid=polling_unit.polling_unit_id,
                        party_abbreviation=party_abbreviation,
                        party_score=int(party_score),
                        entered_by_user=request.user.username,
                        date_entered=datetime.now(),
                        user_ip_address=request.META['REMOTE_ADDR']
                    )
                    result_obj.save()
                except ValueError:
                    messages.error(request, f"Invalid data format: {result}. Please enter party results in the format 'Party Abbreviation:Party Score'.")
                    return redirect('add_polling_unit_result')

            return redirect('polling_unit_results')
    else:
        form = PollingUnitResultForm()

    results = AnnouncedPuResults.objects.all()
    polling_units = PollingUnit.objects.all()

    context = {
        'form': form,
        'results': results,
        'polling_units': polling_units,
    }

    return render(request, 'results/polling_unit_results.html', context)
