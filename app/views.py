from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from .models import User
def Home(request):
    return render(request,'app/Home.html')

def Login(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully!")
            return redirect('/Home')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/Login.html', {'form': form})

def logintest(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully!")
            return redirect('/Home')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/logintest.html', {'form': form})


def Signin(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    messages.success(request, "Login successful!")
                    return redirect('/Home')
                else:
                    messages.error(request, "Invalid password.")
            except User.DoesNotExist:
                messages.error(request, "User not found.")
    
    else:
        form = UserLoginForm()
    return render(request, 'app/Signin.html', {'form': form})

def About(request):
    if request.method == 'POST':
        pass
    return render(request,'app/About.html')

def Contact(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Contact.html')

def Aston_martin_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Aston_martin_model.html')

def Audi_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_model.html')

def Bentley_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Bentley_model.html')

def BMW_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_model.html')

def BYD_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BYD_model.html')

def Ferrari_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Ferrari_model.html')

def Honda_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Honda_model.html')

def Hyundai_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_model.html')

def Jaguar_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Jaguar_model.html')

def Jeep_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Jeep_model.html')

def Kia_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Kia_model.html')

def Lamborghini_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Lamborghini_model.html')

def Land_rover(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Land_rover.html')

def Lexus_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Lexus_model.html')

def Mahindra_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mahindra_model.html')

def Maserati_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Maserati_model.html')

def McLaren_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/McLaren_model.html')

def Mercedes_benz_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_model.html')

def Mg_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mg_model.html')

def Mini_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mini_model.html')

def Nissan_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Nissan_model.html')

def Prosche_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Prosche_model.html')

def Renault_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Renault_model.html')

def Rolls_royce(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Rolls_royce.html')

def Skoda_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Skoda_model.html')

def suzuki_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/suzuki_model.html')

def Tata_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_model.html')

def Toyota_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_model.html')

def Volkswagen_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Volkswagen_model.html')

def Volvo_model(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Volvo_model.html')

def Aston_martin_DB12_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Aston_martin_DB12_full_detail.html')

def Aston_martin_DBX_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Aston_martin_DBX_full_detail.html')

def Aston_martin_vantage_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Aston_martin_vantage_full_detail.html')

def Audi_A4_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_A4_full_detail.html')

def Audi_A6_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_A6_full_detail.html')

def Audi_A8L_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_A8L_full_detail.html')

def Audi_Q3_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_Q3_full_detail.html')

def Audi_Q3_sportback_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_Q3_sportback_full_detail.html')

def Audi_Q5_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_Q5_full_detail.html')

def Audi_Q7_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_Q7_full_detail.html')

def Audi_Q8_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_Q8_full_detail.html')

def Audi_Q8_etron_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_Q8_etron_full_detail.html')

def Audi_etron_GT_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_etron_GT_full_detail.html')

def Audi_RS5_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_RS5_full_detail.html')

def Audi_S5_sportback_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Audi_S5_sportback_full_detail.html')

def Bentley_bentayga_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Bentley_bentayga_full_detail.html')

def Bentley_continental_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Bentley_continental_full_detail.html')

def Bentley_flying_spur_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Bentley_flying_spur_full_detail.html')

def BMW_2_series_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_2_series_full_detail.html')

def BMW_3_series_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_3_series_full_detail.html')

def BMW_5_series_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_5_series_full_detail.html')

def BMW_6_series_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_6_series_full_detail.html')

def BMW_7_series_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_7_series_full_detail.html')

def BMW_i4_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_i4_full_detail.html')

def BMW_i5_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_i5_full_detail.html')

def BMW_i7_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_i7_full_detail.html')

def BMW_ix_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_ix_full_detail.html')

def BMW_m2_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_m2_full_detail.html')

def BMW_M4_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_M4_full_detail.html')

def BMW_M5_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_M5_full_detail.html')

def BMW_m8_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_m8_full_detail.html')

def BMW_x1_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_x1_full_detail.html')

def BMW_x3_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_x3_full_detail.html')

def BMW_x4_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_x4_full_detail.html')

def BMW_x5_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_x5_full_detail.html')

def BMW_x7_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_x7_full_detail.html')

def BMW_xm_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_xm_full_detail.html')

def BMW_z4_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BMW_z4_full_detail.html')

def BYD_atto_3_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BYD_atto_3_full_detail.html')

def BYD_emax_7_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BYD_emax_7_full_detail.html')

def BYD_seal_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/BYD_seal_full_detail.html')

def Ferrari_296_gtb_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Ferrari_296_gtb_full_detail.html')

def Ferrari_812_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Ferrari_812_full_detail.html')

def Ferrari_f8_tributo_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Ferrari_f8_tributo_full_detail.html')

def Ferrari_roma_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Ferrari_roma_full_detail.html')

def Ferrari_sf90_stradale_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Ferrari_sf90_stradale_full_detail.html')

def Honda_amaze_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Honda_amaze_full_detail.html')

def Honda_city_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Honda_city_full_detail.html')

def Honda_city_hybrid_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Honda_city_hybrid_full_detail.html')

def Honda_elevate_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Honda_elevate_full_detail.html')

def Hyundai_alcazar_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_alcazar_full_detail.html')

def Hyundai_aura_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_aura_full_detail.html')

def Hyundai_creta_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_creta_full_detail.html')

def Hyundai_creta_ev_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_creta_ev_full_detail.html')

def Hyundai_exter_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_exter_full_detail.html')

def Hyundai_grand_i10_nios_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_grand_i10_nios_full_detail.html')

def Hyundai_i20_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_i20_full_detail.html')

def Hyundai_ioniq_5_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_ioniq_5_full_detail.html')

def Hyundai_tucson_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_tucson_full_detail.html')

def Hyundai_verna_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_verna_full_detail.html')

def Hyundai_venue_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Hyundai_venue_full_detail.html')

def Jaguar_f_pace_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Jaguar_f_pace_full_detail.html')

def Jeep_compass_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Jeep_compass_full_detail.html')

def Jeep_grand_cherokee_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Jeep_grand_cherokee_full_detail.html')

def Jeep_meridian_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Jeep_meridian_full_detail.html')

def Jeep_wrangler_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Jeep_wrangler_full_detail.html')

def Kia_carens_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Kia_carens_full_detail.html')

def Kia_carnival_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Kia_carnival_full_detail.html')

def Kia_ev6_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Kia_ev6_full_detail.html')

def Kia_ev9_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Kia_ev9_full_detail.html')

def Kia_seltos_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Kia_seltos_full_detail.html')

def Kia_sonet_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Kia_sonet_full_detail.html')

def Kia_syros_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Kia_syros_full_detail.html')

def Lambo_huracan_evo_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Lambo_huracan_evo_full_detail.html')

def Lambo_revuelto_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Lambo_revuelto_full_detail.html')

def Lambo_urus_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Lambo_urus_full_detail.html')

def Land_rover_defender_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Land_rover_defender_full_detail.html')

def Land_rover_discovery_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Land_rover_discovery_full_detail.html')

def Land_rover_discovery_sport_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Land_rover_discovery_sport_full_detail.html')

def Land_rover_evoque_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Land_rover_evoque_full_detail.html')

def Land_rover_velar_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Land_rover_velar_full_detail.html')

def Land_rover_sport_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Land_rover_sport_full_detail.html')

def Land_rover_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Land_rover_full_detail.html')

def Lexus_es_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Lexus_es_full_detail.html')

def Lexus_lm_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Lexus_lm_full_detail.html')

def Lexus_lx_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Lexus_lx_full_detail.html')

def Lexus_nx_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Lexus_nx_full_detail.html')

def Lexus_rx_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Lexus_rx_full_detail.html')

def Mahindra_be6_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mahindra_be6_full_detail.html')

def Mahindra_bolero_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mahindra_bolero_full_detail.html')

def Mahindra_bolero_camper_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mahindra_bolero_camper_full_detail.html')

def Mahindra_bolero_neo_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mahindra_bolero_neo_full_detail.html')

def Mahindra_scorpio_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mahindra_scorpio_full_detail.html')

def Mahindra_scorpio_n_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mahindra_scorpio_n_full_detail.html')

def Mahindra_thar_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mahindra_thar_full_detail.html')

def Mahindra_thar_roxx_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mahindra_thar_roxx_full_detail.html')

def Maserati_ghibli_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Maserati_ghibli_full_detail.html')

def Maserati_grancabrio_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Maserati_grancabrio_full_detail.html')

def Maserati_granturismo_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Maserati_granturismo_full_detail.html')

def Maserati_grecale_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Maserati_grecale_full_detail.html')

def Maserati_levante_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Maserati_levante_full_detail.html')

def Maserati_quattroporte_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Maserati_quattroporte_full_detail.html')

def McLaren_gt_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/McLaren_gt_full_detail.html')

def McLaren_750s_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/McLaren_750s_full_detail.html')

def Mercedes_benz_a_class_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_a_class_full_detail.html')

def Mercedes_benz_amg_e53_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_amg_e53_full_detail.html')

def Mercedes_benz_amg_glc43_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_amg_glc43_full_detail.html')

def Mercedes_benz_amg_gle53_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_amg_gle53_full_detail.html')

def Mercedes_benz_amg_gt_4_door_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_amg_gt_4_door_full_detail.html')

def Mercedes_benz_amg_sl_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_amg_sl_full_detail.html')

def Mercedes_benz_c_class_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_c_class_full_detail.html')

def Mercedes_benz_cle_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_cle_full_detail.html')

def Mercedes_benz_e_class_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_e_class_full_detail.html')

def Mercedes_benz_eqa_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_eqa_full_detail.html')

def Mercedes_benz_eqb_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_eqb_full_detail.html')

def Mercedes_benz_eqe_suv_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_eqe_suv_full_detail.html')

def Mercedes_benz_eqs_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_eqs_full_detail.html')

def Mercedes_benz_eqs_suv_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_eqs_suv_full_detail.html')

def Mercedes_benz_maybach_eqs_suv_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_maybach_eqs_suv_full_detail.html')

def Mercedes_benz_g_class_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_g_class_full_detail.html')

def Mercedes_benz_g_class_ele_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_g_class_ele_full_detail.html')

def Mercedes_benz_gla_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_gla_full_detail.html')

def Mercedes_benz_glb_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_glb_full_detail.html')

def Mercedes_benz_glc_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_glc_full_detail.html')

def Mercedes_benz_gle_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_gle_full_detail.html')

def Mercedes_benz_gls_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_gls_full_detail.html')

def Mercedes_benz_maybach_gls_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_maybach_gls_full_detail.html')

def Mercedes_benz_maybach_sclass_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_maybach_sclass_full_detail.html')

def Mercedes_benz_s_class_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mercedes_benz_s_class_full_detail.html')

def Mg_astor_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mg_astor_full_detail.html')

def Mg_comet_ev_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mg_comet_ev_full_detail.html')

def Mg_gloster_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mg_gloster_full_detail.html')

def Mg_hector_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mg_hector_full_detail.html')

def Mg_windsor_ev_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mg_windsor_ev_full_detail.html')

def Mg_zs_ev_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mg_zs_ev_full_detail.html')

def Mini_cooper_3_door_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mini_cooper_3_door_full_detail.html')

def Mini_cooper_countryman_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mini_cooper_countryman_full_detail.html')

def Mini_cooper_s_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mini_cooper_s_full_detail.html')

def Mini_cooper_se_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mini_cooper_se_full_detail.html')

def Mini_countryman_electric_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Mini_countryman_electric_full_detail.html')

def Nissan_magnite_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Nissan_magnite_full_detail.html')

def Nissan_x_trail_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Nissan_x_trail_full_detail.html')

def Porsche_911_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Porsche_911_full_detail.html')

def Porsche_cayenne_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Porsche_cayenne_full_detail.html')

def Porsche_cayenne_coupe_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Porsche_cayenne_coupe_full_detail.html')

def Porsche_macan_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Porsche_macan_full_detail.html')

def Porsche_macan_ev_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Porsche_macan_ev_full_detail.html')

def Porsche_panamera_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Porsche_panamera_full_detail.html')

def Porsche_taycan_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Porsche_taycan_full_detail.html')

def Renault_kiger_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Renault_kiger_full_detail.html')

def Renault_kwid_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Renault_kwid_full_detail.html')

def Renault_triber_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Renault_triber_full_detail.html')

def Rolls_royce_cullinan_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Rolls_royce_cullinan_full_detail.html')

def Rolls_royce_ghost_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Rolls_royce_ghost_full_detail.html')

def Rolls_royce_phantom_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Rolls_royce_phantom_full_detail.html')

def Rolls_royce_spectre_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Rolls_royce_spectre_full_detail.html')

def Skoda_kodiaq_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Skoda_kodiaq_full_detail.html')

def Skoda_kushaq_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Skoda_kushaq_full_detail.html')

def Skoda_kylaq_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Skoda_kylaq_full_detail.html')

def Skoda_slavia_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Skoda_slavia_full_detail.html')

def Skoda_superb_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Skoda_superb_full_detail.html')

def Suzuki_alto_k10_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_alto_k10_full_detail.html')

def Suzuki_baleno_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_baleno_full_detail.html')

def Suzuki_brezza_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_brezza_full_detail.html')

def Suzuki_celerio_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_celerio_full_detail.html')

def Suzuki_ciaz_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_ciaz_full_detail.html')

def Suzuki_dzire_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_dzire_full_detail.html')

def Suzuki_eeco_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_eeco_full_detail.html')

def Suzuki_ertiga_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_ertiga_full_detail.html')

def Suzuki_fronx_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_fronx_full_detail.html')

def Suzuki_grand_vitara_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_grand_vitara_full_detail.html')

def Suzuki_ignis_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_ignis_full_detail.html')

def Suzuki_invicto_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_invicto_full_detail.html')

def Suzuki_jimny_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_jimny_full_detail.html')

def Suzuki_s_presso_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_s_presso_full_detail.html')

def Suzuki_swift_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_swift_full_detail.html')

def Suzuki_wagonr_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_wagonr_full_detail.html')

def Suzuki_xl6_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Suzuki_xl6_full_detail.html')

def Tata_altroz_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_altroz_full_detail.html')

def Tata_curvv_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_curvv_full_detail.html')

def Tata_curvv_ev_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_curvv_ev_full_detail.html')

def Tata_harrier_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_harrier_full_detail.html')

def Tata_nexon_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_nexon_full_detail.html')

def Tata_nexon_ev_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_nexon_ev_full_detail.html')

def Tata_punch_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_punch_full_detail.html')

def Tata_punch_ev_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_punch_ev_full_detail.html')

def Tata_safari_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_safari_full_detail.html')

def Tata_tiago_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_tiago_full_detail.html')

def Tata_tiago_ev_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_tiago_ev_full_detail.html')

def Tata_tigor_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_tigor_full_detail.html')

def Tata_tigor_ev_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Tata_tigor_ev_full_detail.html')

def Toyota_camry_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_camry_full_detail.html')

def Toyota_fortuner_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_fortuner_full_detail.html')

def Toyota_fortuner_legender_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_fortuner_legender_full_detail.html')

def Toyota_glanza_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_glanza_full_detail.html')

def Toyota_hilux_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_hilux_full_detail.html')

def Toyota_innova_crysta_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_innova_crysta_full_detail.html')

def Toyota_innova_hycross_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_innova_hycross_full_detail.html')

def Toyota_land_cruiser_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_land_cruiser_full_detail.html')

def Toyota_rumion_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_rumion_full_detail.html')

def Toyota_taisor_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_taisor_full_detail.html')

def Toyota_urban_cruiser_hyryder_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_urban_cruiser_hyryder_full_detail.html')

def Toyota_vellfire_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Toyota_vellfire_full_detail.html')

def Volkswagen_taigun_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Volkswagen_taigun_full_detail.html')

def Volkswagen_tigaun_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Volkswagen_tigaun_full_detail.html')

def Volkswagen_virtus_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Volkswagen_virtus_full_detail.html')

def Volvo_c40_recharge_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Volvo_c40_recharge_full_detail.html')

def Volvo_ex40_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Volvo_ex40_full_detail.html')

def Volvo_s90_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Volvo_s90_full_detail.html')

def Volvo_xc60_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Volvo_xc60_full_detail.html')

def Volvo_xc90_full_detail(request):
    if request.method == 'POST':
        pass
    return render(request,'app/Volvo_xc90_full_detail.html')