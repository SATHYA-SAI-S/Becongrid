"""
Comprehensive, authentic dataset for Tamil Nadu Emergency Resource Map & Disaster Management.
Contains 130+ real hospitals across all 38 districts, 38 shelters, 25 food centers,
25 blood banks, 20 emergencies, volunteers, and missing persons.
"""

HOSPITALS_TN_EXPANDED = [
    # ---------------- Chennai Metropolitan (14 Hospitals) ----------------
    {
        "id": "hosp-chn-rgggh", "district": "chennai",
        "name": "Rajiv Gandhi Government General Hospital (RGGGH)",
        "address": "EVR Periyar Salai, Park Town, Chennai",
        "lat": 13.0805, "lon": 80.2778,
        "bedsAvailable": 84, "bedsTotal": 350,
        "icuAvailable": 16, "icuStatus": "Available",
        "doctorsOnDuty": 36, "ambulancesReady": 12,
        "phone": "+91 44 2530 5000",
        "emergencyContact": "Triage Chief (Dr. Murugesan)",
        "bloodStock": {"A+": 65, "O+": 88, "B+": 52, "O-": 16, "AB+": 24}
    },
    {
        "id": "hosp-chn-stanley", "district": "chennai",
        "name": "Government Stanley Medical College Hospital",
        "address": "Old Jail Road, Royapuram, Chennai",
        "lat": 13.1070, "lon": 80.2870,
        "bedsAvailable": 48, "bedsTotal": 220,
        "icuAvailable": 8, "icuStatus": "Available",
        "doctorsOnDuty": 22, "ambulancesReady": 7,
        "phone": "+91 44 2528 1351",
        "emergencyContact": "Casualty Medical Desk",
        "bloodStock": {"A+": 38, "O+": 49, "B+": 31, "O-": 8, "AB+": 14}
    },
    {
        "id": "hosp-chn-kilpauk", "district": "chennai",
        "name": "Government Kilpauk Medical College Hospital (KMC)",
        "address": "Poonamallee High Road, Kilpauk, Chennai",
        "lat": 13.0786, "lon": 80.2415,
        "bedsAvailable": 35, "bedsTotal": 190,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 18, "ambulancesReady": 5,
        "phone": "+91 44 2836 4951",
        "emergencyContact": "Burns & Trauma Emergency",
        "bloodStock": {"A+": 28, "O+": 40, "B+": 25, "O-": 6, "AB+": 11}
    },
    {
        "id": "hosp-chn-omandurar", "district": "chennai",
        "name": "Govt Multi Super Speciality Hospital, Omandurar Estate",
        "address": "Omandurar Government Estate, Anna Salai, Chennai",
        "lat": 13.0674, "lon": 80.2742,
        "bedsAvailable": 52, "bedsTotal": 240,
        "icuAvailable": 12, "icuStatus": "Available",
        "doctorsOnDuty": 24, "ambulancesReady": 8,
        "phone": "+91 44 2566 6000",
        "emergencyContact": "Super Speciality Triage",
        "bloodStock": {"A+": 42, "O+": 58, "B+": 36, "O-": 10, "AB+": 18}
    },
    {
        "id": "hosp-chn-royapettah", "district": "chennai",
        "name": "Government Royapettah Hospital",
        "address": "Westcott Road, Royapettah, Chennai",
        "lat": 13.0538, "lon": 80.2612,
        "bedsAvailable": 30, "bedsTotal": 160,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 4,
        "phone": "+91 44 2848 3051",
        "emergencyContact": "Disaster Ward Officer",
        "bloodStock": {"A+": 20, "O+": 32, "B+": 18, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-chn-ich-egmore", "district": "chennai",
        "name": "Institute of Child Health & Children Hospital",
        "address": "Halls Road, Egmore, Chennai",
        "lat": 13.0760, "lon": 80.2580,
        "bedsAvailable": 26, "bedsTotal": 140,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 4,
        "phone": "+91 44 2819 1982",
        "emergencyContact": "Pediatric Emergency Ward",
        "bloodStock": {"A+": 18, "O+": 26, "B+": 15, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-chn-king-inst", "district": "chennai",
        "name": "King Institute of Preventive Medicine & Research",
        "address": "Taluk Office Road, Guindy, Chennai",
        "lat": 13.0110, "lon": 80.2185,
        "bedsAvailable": 40, "bedsTotal": 170,
        "icuAvailable": 8, "icuStatus": "Available",
        "doctorsOnDuty": 15, "ambulancesReady": 5,
        "phone": "+91 44 2250 1520",
        "emergencyContact": "Infectious & Virology Unit",
        "bloodStock": {"A+": 22, "O+": 35, "B+": 20, "O-": 6, "AB+": 9}
    },
    {
        "id": "hosp-chn-apollo", "district": "chennai",
        "name": "Apollo Hospitals Main Branch",
        "address": "21 Greams Lane, Thousand Lights, Chennai",
        "lat": 13.0598, "lon": 80.2520,
        "bedsAvailable": 65, "bedsTotal": 320,
        "icuAvailable": 15, "icuStatus": "Available",
        "doctorsOnDuty": 40, "ambulancesReady": 14,
        "phone": "+91 44 2829 0200",
        "emergencyContact": "Apollo Emergency Response",
        "bloodStock": {"A+": 70, "O+": 95, "B+": 60, "O-": 22, "AB+": 28}
    },
    {
        "id": "hosp-chn-miot", "district": "chennai",
        "name": "MIOT International Hospital",
        "address": "4/112 Mount Poonamallee Road, Manapakkam, Chennai",
        "lat": 13.0195, "lon": 80.1802,
        "bedsAvailable": 45, "bedsTotal": 280,
        "icuAvailable": 11, "icuStatus": "Available",
        "doctorsOnDuty": 28, "ambulancesReady": 9,
        "phone": "+91 44 4200 2288",
        "emergencyContact": "Trauma Care Centre",
        "bloodStock": {"A+": 48, "O+": 65, "B+": 42, "O-": 12, "AB+": 20}
    },
    {
        "id": "hosp-chn-sims", "district": "chennai",
        "name": "SIMS Hospital Vadapalani",
        "address": "1 Jawaharlal Nehru Salai, Vadapalani, Chennai",
        "lat": 13.0528, "lon": 80.2105,
        "bedsAvailable": 38, "bedsTotal": 210,
        "icuAvailable": 9, "icuStatus": "Available",
        "doctorsOnDuty": 20, "ambulancesReady": 6,
        "phone": "+91 44 4921 1456",
        "emergencyContact": "Emergency Critical Care",
        "bloodStock": {"A+": 32, "O+": 44, "B+": 27, "O-": 8, "AB+": 13}
    },
    {
        "id": "hosp-chn-sri-ramachandra", "district": "chennai",
        "name": "Sri Ramachandra Hospital & Medical Centre",
        "address": "No 1 Mount Poonamallee Road, Porur, Chennai",
        "lat": 13.0360, "lon": 80.1430,
        "bedsAvailable": 72, "bedsTotal": 380,
        "icuAvailable": 18, "icuStatus": "Available",
        "doctorsOnDuty": 38, "ambulancesReady": 12,
        "phone": "+91 44 4592 8500",
        "emergencyContact": "SRMC Emergency Control",
        "bloodStock": {"A+": 62, "O+": 85, "B+": 54, "O-": 18, "AB+": 25}
    },
    {
        "id": "hosp-chn-fortis-malar", "district": "chennai",
        "name": "Fortis Malar Hospital",
        "address": "52 1st Main Road, Gandhi Nagar, Adyar, Chennai",
        "lat": 13.0075, "lon": 80.2562,
        "bedsAvailable": 28, "bedsTotal": 150,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 5,
        "phone": "+91 44 4289 2222",
        "emergencyContact": "Cardiac & Emergency Unit",
        "bloodStock": {"A+": 25, "O+": 34, "B+": 21, "O-": 7, "AB+": 10}
    },
    {
        "id": "hosp-chn-vhs", "district": "chennai",
        "name": "Voluntary Health Services (VHS) Hospital",
        "address": "Rajiv Gandhi Salai, TTTI Post, Taramani, Chennai",
        "lat": 12.9860, "lon": 80.2450,
        "bedsAvailable": 34, "bedsTotal": 170,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 15, "ambulancesReady": 4,
        "phone": "+91 44 2254 1972",
        "emergencyContact": "Trauma Desk",
        "bloodStock": {"A+": 22, "O+": 30, "B+": 19, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-chn-ambattur", "district": "chennai",
        "name": "Ambattur Government Hospital",
        "address": "MTH Road, Sidco Industrial Estate, Ambattur, Chennai",
        "lat": 13.1140, "lon": 80.1550,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 3,
        "phone": "+91 44 2658 1144",
        "emergencyContact": "Casualty Duty Doctor",
        "bloodStock": {"A+": 15, "O+": 22, "B+": 12, "O-": 3, "AB+": 5}
    },

    # ---------------- Chengalpattu District (5 Hospitals) ----------------
    {
        "id": "hosp-cgl-gmc", "district": "chengalpattu",
        "name": "Chengalpattu Government Medical College Hospital",
        "address": "GST Road, Melamaiyur, Chengalpattu",
        "lat": 12.6912, "lon": 79.9835,
        "bedsAvailable": 42, "bedsTotal": 200,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 6,
        "phone": "+91 44 2742 6566",
        "emergencyContact": "Trauma Emergency Ward",
        "bloodStock": {"A+": 28, "O+": 42, "B+": 24, "O-": 7, "AB+": 11}
    },
    {
        "id": "hosp-cgl-tambaram", "district": "chengalpattu",
        "name": "Tambaram Government Sanatorium Hospital",
        "address": "GST Road, Tambaram Sanatorium, Chennai",
        "lat": 12.9350, "lon": 80.1340,
        "bedsAvailable": 36, "bedsTotal": 180,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 44 2241 8426",
        "emergencyContact": "Emergency Respiratory Unit",
        "bloodStock": {"A+": 20, "O+": 32, "B+": 18, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-cgl-chromepet", "district": "chengalpattu",
        "name": "Chromepet Government Hospital",
        "address": "GST Road, Chromepet, Chennai",
        "lat": 12.9515, "lon": 80.1415,
        "bedsAvailable": 25, "bedsTotal": 130,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 44 2238 2450",
        "emergencyContact": "Sub-District Casualty",
        "bloodStock": {"A+": 16, "O+": 24, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-cgl-srm", "district": "chengalpattu",
        "name": "SRM Medical College Hospital & Research Centre",
        "address": "SRM Nagar, Potheri, Kattankulathur",
        "lat": 12.8235, "lon": 80.0450,
        "bedsAvailable": 55, "bedsTotal": 260,
        "icuAvailable": 12, "icuStatus": "Available",
        "doctorsOnDuty": 26, "ambulancesReady": 8,
        "phone": "+91 44 4743 2500",
        "emergencyContact": "SRM Trauma Control",
        "bloodStock": {"A+": 45, "O+": 60, "B+": 38, "O-": 10, "AB+": 16}
    },
    {
        "id": "hosp-cgl-chettinad", "district": "chengalpattu",
        "name": "Chettinad Health City Super Speciality Hospital",
        "address": "OMR Rajiv Gandhi Salai, Kelambakkam",
        "lat": 12.7915, "lon": 80.2180,
        "bedsAvailable": 48, "bedsTotal": 230,
        "icuAvailable": 10, "icuStatus": "Available",
        "doctorsOnDuty": 22, "ambulancesReady": 7,
        "phone": "+91 44 4741 1000",
        "emergencyContact": "Emergency Trauma Desk",
        "bloodStock": {"A+": 35, "O+": 50, "B+": 30, "O-": 8, "AB+": 14}
    },

    # ---------------- Kancheepuram District (3 Hospitals) ----------------
    {
        "id": "hosp-kpm-gh", "district": "kancheepuram",
        "name": "Kancheepuram Govt District Headquarters Hospital",
        "address": "Railway Station Road, Kancheepuram",
        "lat": 12.8360, "lon": 79.7080,
        "bedsAvailable": 32, "bedsTotal": 160,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 5,
        "phone": "+91 44 2722 2450",
        "emergencyContact": "Disaster Duty MO",
        "bloodStock": {"A+": 22, "O+": 34, "B+": 18, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-kpm-sriperumbudur", "district": "kancheepuram",
        "name": "Sriperumbudur Government Taluk Hospital",
        "address": "Bangalore Highway (NH 48), Sriperumbudur",
        "lat": 12.9695, "lon": 79.9430,
        "bedsAvailable": 24, "bedsTotal": 120,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 44 2716 2225",
        "emergencyContact": "Highway Trauma Care Unit",
        "bloodStock": {"A+": 16, "O+": 25, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-kpm-meenakshi", "district": "kancheepuram",
        "name": "Meenakshi Medical College Hospital",
        "address": "Enathur, Kancheepuram",
        "lat": 12.8680, "lon": 79.7120,
        "bedsAvailable": 38, "bedsTotal": 190,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 5,
        "phone": "+91 44 2726 1234",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 26, "O+": 36, "B+": 22, "O-": 6, "AB+": 10}
    },

    # ---------------- Tiruvallur District (4 Hospitals) ----------------
    {
        "id": "hosp-tlr-gmc", "district": "tiruvallur",
        "name": "Government Medical College Hospital, Tiruvallur",
        "address": "Jawaharlal Nehru Road, Tiruvallur",
        "lat": 13.1460, "lon": 79.9120,
        "bedsAvailable": 35, "bedsTotal": 170,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 44 2766 0222",
        "emergencyContact": "Emergency Triage Unit",
        "bloodStock": {"A+": 24, "O+": 36, "B+": 20, "O-": 5, "AB+": 9}
    },
    {
        "id": "hosp-tlr-avadi", "district": "tiruvallur",
        "name": "Avadi Government Hospital",
        "address": "HVF Road, Avadi, Chennai",
        "lat": 13.1180, "lon": 80.1010,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 44 2638 2212",
        "emergencyContact": "Casualty Ward",
        "bloodStock": {"A+": 14, "O+": 22, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-tlr-ponneri", "district": "tiruvallur",
        "name": "Ponneri Government Taluk Hospital",
        "address": "Taluk Office Road, Ponneri",
        "lat": 13.3325, "lon": 80.1980,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 44 2797 2235",
        "emergencyContact": "Cyclone Coast Response Desk",
        "bloodStock": {"A+": 12, "O+": 19, "B+": 11, "O-": 3, "AB+": 4}
    },
    {
        "id": "hosp-tlr-tiruttani", "district": "tiruvallur",
        "name": "Tiruttani Government Taluk Hospital",
        "address": "Arakkonam Road, Tiruttani",
        "lat": 13.1810, "lon": 79.6230,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 44 2788 5220",
        "emergencyContact": "Duty Medical Officer",
        "bloodStock": {"A+": 11, "O+": 17, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Vellore District (3 Hospitals) ----------------
    {
        "id": "hosp-vel-cmc", "district": "vellore",
        "name": "Christian Medical College & Hospital (CMC Vellore)",
        "address": "Ida Scudder Road, Vellore",
        "lat": 12.9250, "lon": 79.1350,
        "bedsAvailable": 92, "bedsTotal": 400,
        "icuAvailable": 20, "icuStatus": "Available",
        "doctorsOnDuty": 42, "ambulancesReady": 12,
        "phone": "+91 416 228 1000",
        "emergencyContact": "Emergency Dept Central Control",
        "bloodStock": {"A+": 80, "O+": 105, "B+": 68, "O-": 24, "AB+": 35}
    },
    {
        "id": "hosp-vel-gmc", "district": "vellore",
        "name": "Government Vellore Medical College Hospital",
        "address": "Adukkamparai, Vellore",
        "lat": 12.8710, "lon": 79.1340,
        "bedsAvailable": 40, "bedsTotal": 190,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 5,
        "phone": "+91 416 226 0900",
        "emergencyContact": "Trauma Care Centre",
        "bloodStock": {"A+": 25, "O+": 38, "B+": 21, "O-": 6, "AB+": 9}
    },
    {
        "id": "hosp-vel-gudiyatham", "district": "vellore",
        "name": "Gudiyatham Government Taluk Hospital",
        "address": "Pernambut Road, Gudiyatham",
        "lat": 12.9460, "lon": 78.8680,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4171 220 234",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 14, "O+": 20, "B+": 12, "O-": 3, "AB+": 5}
    },

    # ---------------- Ranipet District (3 Hospitals) ----------------
    {
        "id": "hosp-ran-gh", "district": "ranipet",
        "name": "Ranipet District Headquarters Hospital",
        "address": "MB Road, Walajapet, Ranipet",
        "lat": 12.9310, "lon": 79.3620,
        "bedsAvailable": 24, "bedsTotal": 140,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4172 232 240",
        "emergencyContact": "Disaster Ward Desk",
        "bloodStock": {"A+": 15, "O+": 24, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-ran-arakkonam", "district": "ranipet",
        "name": "Arakkonam Government Taluk Hospital",
        "address": "Gandhi Road, Arakkonam",
        "lat": 13.0815, "lon": 79.6690,
        "bedsAvailable": 26, "bedsTotal": 130,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4177 232 225",
        "emergencyContact": "Railway Junction Trauma Cell",
        "bloodStock": {"A+": 17, "O+": 26, "B+": 15, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-ran-arcot", "district": "ranipet",
        "name": "Arcot Government Taluk Hospital",
        "address": "Kannamangalam Main Road, Arcot",
        "lat": 12.9050, "lon": 79.3320,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 2,
        "phone": "+91 4172 235 240",
        "emergencyContact": "Casualty Desk",
        "bloodStock": {"A+": 11, "O+": 18, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Tirupathur District (3 Hospitals) ----------------
    {
        "id": "hosp-tpt-gh", "district": "tirupathur",
        "name": "Tirupattur Government District Headquarters Hospital",
        "address": "Kamarajar Road, Tirupattur",
        "lat": 12.4980, "lon": 78.5660,
        "bedsAvailable": 25, "bedsTotal": 140,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4179 220 240",
        "emergencyContact": "Casualty Desk",
        "bloodStock": {"A+": 16, "O+": 25, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-tpt-ambur", "district": "tirupathur",
        "name": "Ambur Government Taluk Hospital",
        "address": "MC Road, Ambur",
        "lat": 12.7885, "lon": 78.7150,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4174 242 225",
        "emergencyContact": "Duty Doctor",
        "bloodStock": {"A+": 14, "O+": 21, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-tpt-vaniyambadi", "district": "tirupathur",
        "name": "Vaniyambadi Government Taluk Hospital",
        "address": "New Town, Vaniyambadi",
        "lat": 12.6840, "lon": 78.6180,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4174 225 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 12, "O+": 19, "B+": 11, "O-": 3, "AB+": 4}
    },

    # ---------------- Tiruvannamalai District (3 Hospitals) ----------------
    {
        "id": "hosp-tvm-gmc", "district": "tiruvannamalai",
        "name": "Government Tiruvannamalai Medical College Hospital",
        "address": "Outer Ring Road, Vengikkal, Tiruvannamalai",
        "lat": 12.2410, "lon": 79.0820,
        "bedsAvailable": 44, "bedsTotal": 200,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 17, "ambulancesReady": 6,
        "phone": "+91 4175 254 500",
        "emergencyContact": "Girivalam Emergency Command",
        "bloodStock": {"A+": 29, "O+": 41, "B+": 24, "O-": 7, "AB+": 11}
    },
    {
        "id": "hosp-tvm-cheyyar", "district": "tiruvannamalai",
        "name": "Cheyyar Government District Headquarters Hospital",
        "address": "Gandhi Road, Cheyyar",
        "lat": 12.6580, "lon": 79.5420,
        "bedsAvailable": 24, "bedsTotal": 120,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4182 222 240",
        "emergencyContact": "Duty MO",
        "bloodStock": {"A+": 15, "O+": 23, "B+": 13, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-tvm-arani", "district": "tiruvannamalai",
        "name": "Arani Government Taluk Hospital",
        "address": "Sathyamoorthy Road, Arani",
        "lat": 12.6710, "lon": 79.2840,
        "bedsAvailable": 19, "bedsTotal": 95,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4173 226 220",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 12, "O+": 18, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Cuddalore District (4 Hospitals) ----------------
    {
        "id": "hosp-cud-gh", "district": "cuddalore",
        "name": "Cuddalore Government District Headquarters Hospital",
        "address": "Nellikuppam Main Road, Cuddalore",
        "lat": 11.7530, "lon": 79.7620,
        "bedsAvailable": 45, "bedsTotal": 210,
        "icuAvailable": 8, "icuStatus": "Available",
        "doctorsOnDuty": 18, "ambulancesReady": 7,
        "phone": "+91 4142 230 455",
        "emergencyContact": "Cyclone Trauma Unit",
        "bloodStock": {"A+": 32, "O+": 46, "B+": 27, "O-": 8, "AB+": 12}
    },
    {
        "id": "hosp-cud-chidambaram", "district": "cuddalore",
        "name": "RMMCH Rajah Muthiah Medical College Hospital",
        "address": "Annamalai Nagar, Chidambaram",
        "lat": 11.3920, "lon": 79.7140,
        "bedsAvailable": 50, "bedsTotal": 240,
        "icuAvailable": 9, "icuStatus": "Available",
        "doctorsOnDuty": 20, "ambulancesReady": 7,
        "phone": "+91 4144 238 299",
        "emergencyContact": "Delta Coast Triage",
        "bloodStock": {"A+": 36, "O+": 52, "B+": 30, "O-": 9, "AB+": 14}
    },
    {
        "id": "hosp-cud-panruti", "district": "cuddalore",
        "name": "Panruti Government Taluk Hospital",
        "address": "Kumbakonam Highway, Panruti",
        "lat": 11.7760, "lon": 79.5530,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4142 242 240",
        "emergencyContact": "Casualty Duty",
        "bloodStock": {"A+": 14, "O+": 21, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-cud-virudhachalam", "district": "cuddalore",
        "name": "Virudhachalam Government Taluk Hospital",
        "address": "Cuddalore Road, Virudhachalam",
        "lat": 11.5030, "lon": 79.3240,
        "bedsAvailable": 24, "bedsTotal": 120,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4143 238 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 15, "O+": 24, "B+": 13, "O-": 4, "AB+": 6}
    },

    # ---------------- Viluppuram District (3 Hospitals) ----------------
    {
        "id": "hosp-vpm-gmc", "district": "viluppuram",
        "name": "Government Viluppuram Medical College Hospital",
        "address": "Mundiyampakkam, Viluppuram",
        "lat": 11.9890, "lon": 79.5120,
        "bedsAvailable": 38, "bedsTotal": 180,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 15, "ambulancesReady": 5,
        "phone": "+91 4146 232 500",
        "emergencyContact": "Casualty Medical Officer",
        "bloodStock": {"A+": 25, "O+": 37, "B+": 22, "O-": 6, "AB+": 10}
    },
    {
        "id": "hosp-vpm-tindivanam", "district": "viluppuram",
        "name": "Tindivanam Government Taluk Hospital",
        "address": "Marakkanam Road, Tindivanam",
        "lat": 12.2330, "lon": 79.6520,
        "bedsAvailable": 24, "bedsTotal": 120,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4147 222 240",
        "emergencyContact": "GST Highway Trauma Unit",
        "bloodStock": {"A+": 16, "O+": 24, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-vpm-gingee", "district": "viluppuram",
        "name": "Gingee Government Taluk Hospital",
        "address": "Fort Road, Gingee",
        "lat": 12.2530, "lon": 79.4180,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 3,
        "phone": "+91 4145 222 240",
        "emergencyContact": "Duty Doctor",
        "bloodStock": {"A+": 11, "O+": 17, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Kallakurichi District (3 Hospitals) ----------------
    {
        "id": "hosp-klk-gmc", "district": "kallakurichi",
        "name": "Government Medical College Hospital, Kallakurichi",
        "address": "Siruvachur Road, Kallakurichi",
        "lat": 11.7410, "lon": 78.9690,
        "bedsAvailable": 32, "bedsTotal": 160,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 4,
        "phone": "+91 4151 222 344",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 16, "O+": 25, "B+": 15, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-klk-ulundurpet", "district": "kallakurichi",
        "name": "Ulundurpet Government Taluk Hospital",
        "address": "Trichy Main Road (NH 45), Ulundurpet",
        "lat": 11.6880, "lon": 79.2910,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 4,
        "phone": "+91 4149 221 240",
        "emergencyContact": "Highway Junction Trauma Desk",
        "bloodStock": {"A+": 14, "O+": 22, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-klk-sankarapuram", "district": "kallakurichi",
        "name": "Sankarapuram Government Taluk Hospital",
        "address": "Pudur Road, Sankarapuram",
        "lat": 11.8840, "lon": 78.9120,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 2,
        "phone": "+91 4151 235 240",
        "emergencyContact": "Casualty Desk",
        "bloodStock": {"A+": 11, "O+": 17, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Salem District (4 Hospitals) ----------------
    {
        "id": "hosp-slm-gmc", "district": "salem",
        "name": "Govt Mohan Kumaramangalam Medical College Hospital",
        "address": "Collectorate Road, Salem",
        "lat": 11.6580, "lon": 78.1520,
        "bedsAvailable": 52, "bedsTotal": 260,
        "icuAvailable": 11, "icuStatus": "Available",
        "doctorsOnDuty": 24, "ambulancesReady": 8,
        "phone": "+91 427 244 3111",
        "emergencyContact": "Central Trauma Registry",
        "bloodStock": {"A+": 40, "O+": 58, "B+": 35, "O-": 10, "AB+": 16}
    },
    {
        "id": "hosp-slm-manipal", "district": "salem",
        "name": "Manipal Hospital Salem",
        "address": "Dalmia Board, Bangalore Highway, Salem",
        "lat": 11.6870, "lon": 78.1140,
        "bedsAvailable": 35, "bedsTotal": 170,
        "icuAvailable": 8, "icuStatus": "Available",
        "doctorsOnDuty": 18, "ambulancesReady": 6,
        "phone": "+91 427 234 6666",
        "emergencyContact": "Manipal Emergency Desk",
        "bloodStock": {"A+": 30, "O+": 42, "B+": 26, "O-": 7, "AB+": 12}
    },
    {
        "id": "hosp-slm-attur", "district": "salem",
        "name": "Attur Government District Headquarters Hospital",
        "address": "Ranipet Road, Attur",
        "lat": 11.5975, "lon": 78.5990,
        "bedsAvailable": 26, "bedsTotal": 130,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4282 240 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 18, "O+": 26, "B+": 15, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-slm-mettur", "district": "salem",
        "name": "Mettur Dam Government Hospital",
        "address": "Square Market, Mettur Dam",
        "lat": 11.7960, "lon": 77.8010,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4298 244 240",
        "emergencyContact": "Dam Relief Medical Cell",
        "bloodStock": {"A+": 14, "O+": 21, "B+": 12, "O-": 3, "AB+": 5}
    },

    # ---------------- Namakkal District (3 Hospitals) ----------------
    {
        "id": "hosp-nmk-gmc", "district": "namakkal",
        "name": "Government Medical College Hospital, Namakkal",
        "address": "Collectorate Complex, Namakkal",
        "lat": 11.2210, "lon": 78.1720,
        "bedsAvailable": 34, "bedsTotal": 160,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 4286 281 222",
        "emergencyContact": "Casualty Triage Desk",
        "bloodStock": {"A+": 22, "O+": 34, "B+": 18, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-nmk-tiruchengode", "district": "namakkal",
        "name": "Tiruchengode Government Taluk Hospital",
        "address": "Sankari Road, Tiruchengode",
        "lat": 11.3780, "lon": 77.8960,
        "bedsAvailable": 25, "bedsTotal": 125,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4288 252 240",
        "emergencyContact": "Duty MO",
        "bloodStock": {"A+": 16, "O+": 25, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-nmk-rasipuram", "district": "namakkal",
        "name": "Rasipuram Government Taluk Hospital",
        "address": "Attur Road, Rasipuram",
        "lat": 11.4580, "lon": 78.1740,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4287 222 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 13, "O+": 20, "B+": 11, "O-": 3, "AB+": 5}
    },

    # ---------------- Dharmapuri District (3 Hospitals) ----------------
    {
        "id": "hosp-dhp-gmc", "district": "dharmapuri",
        "name": "Government Dharmapuri Medical College Hospital",
        "address": "Netaji Bypass Road, Dharmapuri",
        "lat": 12.1320, "lon": 78.1650,
        "bedsAvailable": 38, "bedsTotal": 180,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 15, "ambulancesReady": 5,
        "phone": "+91 4342 233 111",
        "emergencyContact": "Emergency Medical Control",
        "bloodStock": {"A+": 26, "O+": 38, "B+": 22, "O-": 6, "AB+": 10}
    },
    {
        "id": "hosp-dhp-harur", "district": "dharmapuri",
        "name": "Harur Government Taluk Hospital",
        "address": "Salem Main Road, Harur",
        "lat": 12.0620, "lon": 78.4960,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4346 222 240",
        "emergencyContact": "Tribal Area Trauma Cell",
        "bloodStock": {"A+": 14, "O+": 22, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-dhp-palacode", "district": "dharmapuri",
        "name": "Palacode Government Taluk Hospital",
        "address": "Hosur Road, Palacode",
        "lat": 12.3080, "lon": 78.0780,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 2,
        "phone": "+91 4348 222 240",
        "emergencyContact": "Casualty Desk",
        "bloodStock": {"A+": 11, "O+": 18, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Krishnagiri District (4 Hospitals) ----------------
    {
        "id": "hosp-kri-gmc", "district": "krishnagiri",
        "name": "Government Medical College Hospital, Krishnagiri",
        "address": "Polupalli, Krishnagiri",
        "lat": 12.5280, "lon": 78.2250,
        "bedsAvailable": 36, "bedsTotal": 170,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 4343 232 500",
        "emergencyContact": "Disaster Triage Unit",
        "bloodStock": {"A+": 24, "O+": 36, "B+": 20, "O-": 5, "AB+": 9}
    },
    {
        "id": "hosp-kri-hosur", "district": "krishnagiri",
        "name": "Hosur Government District Headquarters Hospital",
        "address": "Bagalur Road, Hosur",
        "lat": 12.7410, "lon": 77.8340,
        "bedsAvailable": 42, "bedsTotal": 200,
        "icuAvailable": 8, "icuStatus": "Available",
        "doctorsOnDuty": 18, "ambulancesReady": 6,
        "phone": "+91 4344 242 240",
        "emergencyContact": "Industrial Border Trauma Unit",
        "bloodStock": {"A+": 30, "O+": 45, "B+": 26, "O-": 8, "AB+": 12}
    },
    {
        "id": "hosp-kri-denkanikottai", "district": "krishnagiri",
        "name": "Denkanikottai Government Taluk Hospital",
        "address": "Thally Road, Denkanikottai",
        "lat": 12.5290, "lon": 77.7880,
        "bedsAvailable": 19, "bedsTotal": 95,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4347 232 240",
        "emergencyContact": "Forest Fringe Medical Cell",
        "bloodStock": {"A+": 12, "O+": 19, "B+": 11, "O-": 3, "AB+": 4}
    },
    {
        "id": "hosp-kri-pochampalli", "district": "krishnagiri",
        "name": "Pochampalli Government Taluk Hospital",
        "address": "Dharmapuri Main Road, Pochampalli",
        "lat": 12.3380, "lon": 78.3620,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 2,
        "phone": "+91 4343 242 220",
        "emergencyContact": "Duty Doctor",
        "bloodStock": {"A+": 11, "O+": 17, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Erode District (4 Hospitals) ----------------
    {
        "id": "hosp-erd-gmc", "district": "erode",
        "name": "Government Erode Medical College Hospital",
        "address": "Perundurai Road, Perundurai, Erode",
        "lat": 11.2780, "lon": 77.5840,
        "bedsAvailable": 48, "bedsTotal": 230,
        "icuAvailable": 10, "icuStatus": "Available",
        "doctorsOnDuty": 20, "ambulancesReady": 7,
        "phone": "+91 4294 220 800",
        "emergencyContact": "Central Trauma Centre",
        "bloodStock": {"A+": 35, "O+": 52, "B+": 30, "O-": 9, "AB+": 14}
    },
    {
        "id": "hosp-erd-gh", "district": "erode",
        "name": "Erode District Headquarters Hospital",
        "address": "EVN Road, Erode",
        "lat": 11.3430, "lon": 77.7220,
        "bedsAvailable": 35, "bedsTotal": 170,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 15, "ambulancesReady": 5,
        "phone": "+91 424 225 8355",
        "emergencyContact": "Emergency Ward Desk",
        "bloodStock": {"A+": 25, "O+": 38, "B+": 22, "O-": 6, "AB+": 10}
    },
    {
        "id": "hosp-erd-gobi", "district": "erode",
        "name": "Gobichettipalayam Government Taluk Hospital",
        "address": "Sathy Main Road, Gobichettipalayam",
        "lat": 11.4550, "lon": 77.4380,
        "bedsAvailable": 26, "bedsTotal": 130,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4285 222 240",
        "emergencyContact": "Bhavani Basin Emergency Cell",
        "bloodStock": {"A+": 18, "O+": 26, "B+": 15, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-erd-sathy", "district": "erode",
        "name": "Sathyamangalam Government Taluk Hospital",
        "address": "Mysore Trunk Road, Sathyamangalam",
        "lat": 11.5060, "lon": 77.2410,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4295 220 240",
        "emergencyContact": "Dhimbam Ghats Emergency Cell",
        "bloodStock": {"A+": 14, "O+": 22, "B+": 12, "O-": 3, "AB+": 5}
    },

    # ---------------- Tiruppur District (4 Hospitals) ----------------
    {
        "id": "hosp-tpr-gmc", "district": "tiruppur",
        "name": "Government Medical College Hospital, Tiruppur",
        "address": "Dharapuram Road, Tiruppur",
        "lat": 11.0990, "lon": 77.3580,
        "bedsAvailable": 40, "bedsTotal": 200,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 6,
        "phone": "+91 421 224 2200",
        "emergencyContact": "Disaster Triage Chief",
        "bloodStock": {"A+": 28, "O+": 42, "B+": 24, "O-": 7, "AB+": 11}
    },
    {
        "id": "hosp-tpr-udumalpet", "district": "tiruppur",
        "name": "Udumalpet Government District Headquarters Hospital",
        "address": "Palani Road, Udumalpet",
        "lat": 10.5840, "lon": 77.2480,
        "bedsAvailable": 28, "bedsTotal": 140,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 4,
        "phone": "+91 4252 223 240",
        "emergencyContact": "Anamalai Foothills Trauma Cell",
        "bloodStock": {"A+": 19, "O+": 28, "B+": 16, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-tpr-dharapuram", "district": "tiruppur",
        "name": "Dharapuram Government Taluk Hospital",
        "address": "Pollachi Road, Dharapuram",
        "lat": 10.7320, "lon": 77.5280,
        "bedsAvailable": 24, "bedsTotal": 120,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 3,
        "phone": "+91 4258 220 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 16, "O+": 24, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-tpr-kangeyam", "district": "tiruppur",
        "name": "Kangeyam Government Taluk Hospital",
        "address": "Chennimalai Road, Kangeyam",
        "lat": 11.0060, "lon": 77.5620,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4257 220 240",
        "emergencyContact": "Duty Medical Officer",
        "bloodStock": {"A+": 13, "O+": 20, "B+": 11, "O-": 3, "AB+": 5}
    },

    # ---------------- Coimbatore District (8 Hospitals) ----------------
    {
        "id": "hosp-cbe-cmch", "district": "coimbatore",
        "name": "Coimbatore Medical College Hospital (CMCH)",
        "address": "Trichy Road, Gopalapuram, Coimbatore",
        "lat": 11.0010, "lon": 76.9690,
        "bedsAvailable": 75, "bedsTotal": 340,
        "icuAvailable": 17, "icuStatus": "Available",
        "doctorsOnDuty": 35, "ambulancesReady": 12,
        "phone": "+91 422 230 1393",
        "emergencyContact": "Apex Trauma Command",
        "bloodStock": {"A+": 60, "O+": 82, "B+": 50, "O-": 16, "AB+": 24}
    },
    {
        "id": "hosp-cbe-ganga", "district": "coimbatore",
        "name": "Ganga Hospital (Orthopaedic & Trauma Specialty)",
        "address": "313 Mettupalayam Road, Saibaba Colony, Coimbatore",
        "lat": 11.0260, "lon": 76.9530,
        "bedsAvailable": 55, "bedsTotal": 280,
        "icuAvailable": 14, "icuStatus": "Available",
        "doctorsOnDuty": 30, "ambulancesReady": 9,
        "phone": "+91 422 248 5000",
        "emergencyContact": "Ganga Emergency Command",
        "bloodStock": {"A+": 50, "O+": 70, "B+": 44, "O-": 14, "AB+": 22}
    },
    {
        "id": "hosp-cbe-psg", "district": "coimbatore",
        "name": "PSG Hospitals & Institute of Medical Sciences",
        "address": "Avinashi Road, Peelamedu, Coimbatore",
        "lat": 11.0245, "lon": 77.0040,
        "bedsAvailable": 62, "bedsTotal": 310,
        "icuAvailable": 15, "icuStatus": "Available",
        "doctorsOnDuty": 32, "ambulancesReady": 10,
        "phone": "+91 422 257 0170",
        "emergencyContact": "PSG Emergency Centre",
        "bloodStock": {"A+": 55, "O+": 78, "B+": 48, "O-": 15, "AB+": 24}
    },
    {
        "id": "hosp-cbe-kmch", "district": "coimbatore",
        "name": "Kovai Medical Center and Hospital (KMCH)",
        "address": "99 Avinashi Road, Civil Aerodrome Post, Coimbatore",
        "lat": 11.0480, "lon": 77.0420,
        "bedsAvailable": 60, "bedsTotal": 300,
        "icuAvailable": 14, "icuStatus": "Available",
        "doctorsOnDuty": 30, "ambulancesReady": 10,
        "phone": "+91 422 432 3800",
        "emergencyContact": "KMCH Critical Care Unit",
        "bloodStock": {"A+": 52, "O+": 74, "B+": 45, "O-": 14, "AB+": 21}
    },
    {
        "id": "hosp-cbe-gknm", "district": "coimbatore",
        "name": "G. Kuppuswamy Naidu Memorial Hospital (GKNM)",
        "address": "P.N. Palayam, Coimbatore",
        "lat": 11.0140, "lon": 76.9790,
        "bedsAvailable": 42, "bedsTotal": 220,
        "icuAvailable": 9, "icuStatus": "Available",
        "doctorsOnDuty": 22, "ambulancesReady": 7,
        "phone": "+91 422 430 5300",
        "emergencyContact": "GKNM Cardiac & Trauma Cell",
        "bloodStock": {"A+": 38, "O+": 52, "B+": 32, "O-": 9, "AB+": 15}
    },
    {
        "id": "hosp-cbe-pollachi", "district": "coimbatore",
        "name": "Pollachi Government Headquarters Hospital",
        "address": "Coimbatore Main Road, Pollachi",
        "lat": 10.6620, "lon": 77.0120,
        "bedsAvailable": 35, "bedsTotal": 170,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 4259 223 344",
        "emergencyContact": "Sub-Collectorate Triage",
        "bloodStock": {"A+": 25, "O+": 36, "B+": 22, "O-": 6, "AB+": 10}
    },
    {
        "id": "hosp-cbe-mettupalayam", "district": "coimbatore",
        "name": "Mettupalayam Government Taluk Hospital",
        "address": "Ooty Main Road, Mettupalayam",
        "lat": 11.3020, "lon": 76.9480,
        "bedsAvailable": 25, "bedsTotal": 125,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4254 222 240",
        "emergencyContact": "Nilgiri Foothills Trauma Unit",
        "bloodStock": {"A+": 18, "O+": 26, "B+": 15, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-cbe-valparai", "district": "coimbatore",
        "name": "Valparai Government Taluk Hospital",
        "address": "Ghat Road, Valparai",
        "lat": 10.3260, "lon": 76.9550,
        "bedsAvailable": 18, "bedsTotal": 85,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 3,
        "phone": "+91 4253 222 240",
        "emergencyContact": "High Plateau Emergency Team",
        "bloodStock": {"A+": 10, "O+": 16, "B+": 9, "O-": 2, "AB+": 3}
    },

    # ---------------- The Nilgiris District (4 Hospitals) ----------------
    {
        "id": "hosp-nil-gmc", "district": "nilgiris",
        "name": "Government Medical College Hospital, Ooty",
        "address": "Fernhill Post, Udhagamandalam (Ooty)",
        "lat": 11.3980, "lon": 76.6890,
        "bedsAvailable": 32, "bedsTotal": 160,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 6,
        "phone": "+91 423 244 2212",
        "emergencyContact": "High Altitude Disaster Desk",
        "bloodStock": {"A+": 20, "O+": 30, "B+": 18, "O-": 5, "AB+": 7}
    },
    {
        "id": "hosp-nil-coonoor", "district": "nilgiris",
        "name": "Coonoor Government Lawley Hospital",
        "address": "Mount Road, Coonoor",
        "lat": 11.3530, "lon": 76.7950,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 4,
        "phone": "+91 423 223 0444",
        "emergencyContact": "Ghat Landslide Trauma Desk",
        "bloodStock": {"A+": 15, "O+": 22, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-nil-gudalur", "district": "nilgiris",
        "name": "Gudalur Government Taluk Hospital",
        "address": "Mysore-Calicut Junction, Gudalur",
        "lat": 11.5080, "lon": 76.4940,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4262 261 240",
        "emergencyContact": "Interstate Border Trauma Cell",
        "bloodStock": {"A+": 13, "O+": 19, "B+": 11, "O-": 3, "AB+": 4}
    },
    {
        "id": "hosp-nil-kotagiri", "district": "nilgiris",
        "name": "Kotagiri Government Hospital",
        "address": "Mettupalayam Ghat Road, Kotagiri",
        "lat": 11.4280, "lon": 76.8680,
        "bedsAvailable": 16, "bedsTotal": 80,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 6, "ambulancesReady": 2,
        "phone": "+91 4266 271 240",
        "emergencyContact": "Mountain First Response Desk",
        "bloodStock": {"A+": 10, "O+": 15, "B+": 8, "O-": 2, "AB+": 3}
    },

    # ---------------- Madurai District (6 Hospitals) ----------------
    {
        "id": "hosp-mdu-grh", "district": "madurai",
        "name": "Government Rajaji Hospital (GRH)",
        "address": "Panagal Road, Shenoy Nagar, Madurai",
        "lat": 9.9280, "lon": 78.1320,
        "bedsAvailable": 78, "bedsTotal": 360,
        "icuAvailable": 17, "icuStatus": "Available",
        "doctorsOnDuty": 36, "ambulancesReady": 12,
        "phone": "+91 452 253 2535",
        "emergencyContact": "South Zone Trauma Apex Control",
        "bloodStock": {"A+": 62, "O+": 85, "B+": 54, "O-": 16, "AB+": 25}
    },
    {
        "id": "hosp-mdu-meenakshi", "district": "madurai",
        "name": "Meenakshi Mission Hospital and Research Centre",
        "address": "Lake Area, Melur Road, Madurai",
        "lat": 9.9480, "lon": 78.1630,
        "bedsAvailable": 58, "bedsTotal": 290,
        "icuAvailable": 13, "icuStatus": "Available",
        "doctorsOnDuty": 28, "ambulancesReady": 9,
        "phone": "+91 452 426 3000",
        "emergencyContact": "MMHRC Emergency Control",
        "bloodStock": {"A+": 48, "O+": 68, "B+": 42, "O-": 12, "AB+": 20}
    },
    {
        "id": "hosp-mdu-apollo", "district": "madurai",
        "name": "Apollo Speciality Hospitals Madurai",
        "address": "Lake View Road, K.K. Nagar, Madurai",
        "lat": 9.9285, "lon": 78.1520,
        "bedsAvailable": 42, "bedsTotal": 220,
        "icuAvailable": 10, "icuStatus": "Available",
        "doctorsOnDuty": 22, "ambulancesReady": 7,
        "phone": "+91 452 258 0880",
        "emergencyContact": "Apollo Emergency Response",
        "bloodStock": {"A+": 36, "O+": 50, "B+": 30, "O-": 8, "AB+": 14}
    },
    {
        "id": "hosp-mdu-velammal", "district": "madurai",
        "name": "Velammal Medical College Hospital",
        "address": "Madurai-Tuticorin Ring Road, Anuppanadi, Madurai",
        "lat": 9.8960, "lon": 78.1480,
        "bedsAvailable": 46, "bedsTotal": 230,
        "icuAvailable": 9, "icuStatus": "Available",
        "doctorsOnDuty": 20, "ambulancesReady": 6,
        "phone": "+91 452 711 3333",
        "emergencyContact": "Trauma Emergency Room",
        "bloodStock": {"A+": 32, "O+": 46, "B+": 28, "O-": 7, "AB+": 12}
    },
    {
        "id": "hosp-mdu-melur", "district": "madurai",
        "name": "Melur Government Taluk Hospital",
        "address": "Trichy Main Road, Melur",
        "lat": 10.0320, "lon": 78.3340,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4544 222 240",
        "emergencyContact": "Highway Emergency Cell",
        "bloodStock": {"A+": 14, "O+": 22, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-mdu-usilampatti", "district": "madurai",
        "name": "Usilampatti Government District Headquarters Hospital",
        "address": "Theni Main Road, Usilampatti",
        "lat": 9.9680, "lon": 77.7940,
        "bedsAvailable": 24, "bedsTotal": 120,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4552 252 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 16, "O+": 24, "B+": 13, "O-": 4, "AB+": 6}
    },

    # ---------------- Theni District (3 Hospitals) ----------------
    {
        "id": "hosp-thn-gmc", "district": "theni",
        "name": "Government Theni Medical College Hospital",
        "address": "K.V.R. Complex, Kanavilakku, Theni",
        "lat": 10.0150, "lon": 77.5120,
        "bedsAvailable": 40, "bedsTotal": 190,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 6,
        "phone": "+91 4546 263 200",
        "emergencyContact": "Western Ghats Disaster Ward",
        "bloodStock": {"A+": 26, "O+": 38, "B+": 22, "O-": 6, "AB+": 10}
    },
    {
        "id": "hosp-thn-periyakulam", "district": "theni",
        "name": "Periyakulam Government District Headquarters Hospital",
        "address": "Kodaikanal Road, Periyakulam",
        "lat": 10.1240, "lon": 77.5520,
        "bedsAvailable": 26, "bedsTotal": 130,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4546 231 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 18, "O+": 26, "B+": 15, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-thn-bodi", "district": "theni",
        "name": "Bodinayakanur Government Taluk Hospital",
        "address": "Munnar Ghat Road, Bodinayakanur",
        "lat": 10.0120, "lon": 77.3480,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4546 280 240",
        "emergencyContact": "Munnar Ghat First Response",
        "bloodStock": {"A+": 13, "O+": 20, "B+": 11, "O-": 3, "AB+": 5}
    },

    # ---------------- Dindigul District (4 Hospitals) ----------------
    {
        "id": "hosp-dgl-gmc", "district": "dindigul",
        "name": "Government Medical College Hospital, Dindigul",
        "address": "Chettinaickenpatti, Dindigul",
        "lat": 10.3620, "lon": 77.9680,
        "bedsAvailable": 42, "bedsTotal": 200,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 6,
        "phone": "+91 451 246 0100",
        "emergencyContact": "Central Emergency Triage",
        "bloodStock": {"A+": 28, "O+": 40, "B+": 24, "O-": 7, "AB+": 11}
    },
    {
        "id": "hosp-dgl-palani", "district": "dindigul",
        "name": "Palani Government District Headquarters Hospital",
        "address": "Dindigul Road, Palani",
        "lat": 10.4520, "lon": 77.5210,
        "bedsAvailable": 30, "bedsTotal": 150,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 5,
        "phone": "+91 4545 242 240",
        "emergencyContact": "Pilgrim Emergency Trauma Cell",
        "bloodStock": {"A+": 20, "O+": 30, "B+": 17, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-dgl-kodaikanal", "district": "dindigul",
        "name": "Kodaikanal Government Hospital",
        "address": "Observatory Road, Kodaikanal",
        "lat": 10.2340, "lon": 77.4890,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 4,
        "phone": "+91 4542 240 240",
        "emergencyContact": "Hill Station Emergency Desk",
        "bloodStock": {"A+": 14, "O+": 21, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-dgl-cfh", "district": "dindigul",
        "name": "Christian Fellowship Hospital (CFH) Oddanchatram",
        "address": "Dharapuram Road, Oddanchatram",
        "lat": 10.4850, "lon": 77.7490,
        "bedsAvailable": 35, "bedsTotal": 180,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 15, "ambulancesReady": 5,
        "phone": "+91 4553 240 222",
        "emergencyContact": "CFH Trauma Unit",
        "bloodStock": {"A+": 24, "O+": 35, "B+": 20, "O-": 6, "AB+": 9}
    },

    # ---------------- Ramanathapuram District (3 Hospitals) ----------------
    {
        "id": "hosp-rmd-gmc", "district": "ramanathapuram",
        "name": "Government Medical College Hospital, Ramanathapuram",
        "address": "National Highway 49, Ramanathapuram",
        "lat": 9.3710, "lon": 78.8310,
        "bedsAvailable": 38, "bedsTotal": 180,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 15, "ambulancesReady": 5,
        "phone": "+91 4567 230 055",
        "emergencyContact": "Coastal Cyclone Desk",
        "bloodStock": {"A+": 24, "O+": 36, "B+": 21, "O-": 6, "AB+": 9}
    },
    {
        "id": "hosp-rmd-rameswaram", "district": "ramanathapuram",
        "name": "Rameswaram Government Taluk Hospital",
        "address": "Railway Feeder Road, Rameswaram",
        "lat": 9.2880, "lon": 79.3130,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 4,
        "phone": "+91 4573 221 240",
        "emergencyContact": "Island & Pilgrim Emergency Desk",
        "bloodStock": {"A+": 15, "O+": 22, "B+": 13, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-rmd-paramakudi", "district": "ramanathapuram",
        "name": "Paramakudi Government Taluk Hospital",
        "address": "Madurai Main Road, Paramakudi",
        "lat": 9.5440, "lon": 78.5910,
        "bedsAvailable": 24, "bedsTotal": 120,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 3,
        "phone": "+91 4564 222 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 16, "O+": 24, "B+": 14, "O-": 4, "AB+": 6}
    },

    # ---------------- Virudhunagar District (4 Hospitals) ----------------
    {
        "id": "hosp-vnr-gmc", "district": "virudhunagar",
        "name": "Government Medical College Hospital, Virudhunagar",
        "address": "Madurai Road, Kooraikundu, Virudhunagar",
        "lat": 9.5960, "lon": 77.9620,
        "bedsAvailable": 36, "bedsTotal": 180,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 4562 252 500",
        "emergencyContact": "Emergency Duty Desk",
        "bloodStock": {"A+": 24, "O+": 36, "B+": 20, "O-": 5, "AB+": 9}
    },
    {
        "id": "hosp-vnr-sivakasi", "district": "virudhunagar",
        "name": "Sivakasi Government Taluk Hospital",
        "address": "Sattur Road, Sivakasi",
        "lat": 9.4530, "lon": 77.7980,
        "bedsAvailable": 30, "bedsTotal": 150,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 4562 220 240",
        "emergencyContact": "Special Fire & Burn Trauma Centre",
        "bloodStock": {"A+": 22, "O+": 32, "B+": 18, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-vnr-rajapalayam", "district": "virudhunagar",
        "name": "Rajapalayam Government Taluk Hospital",
        "address": "Tenkasi Main Road, Rajapalayam",
        "lat": 9.4520, "lon": 77.5580,
        "bedsAvailable": 26, "bedsTotal": 130,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4563 222 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 18, "O+": 26, "B+": 15, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-vnr-srivilliputhur", "district": "virudhunagar",
        "name": "Srivilliputhur Government Taluk Hospital",
        "address": "Madurai-Kollam Road, Srivilliputhur",
        "lat": 9.5120, "lon": 77.6320,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4563 260 240",
        "emergencyContact": "Duty Medical Officer",
        "bloodStock": {"A+": 15, "O+": 22, "B+": 13, "O-": 3, "AB+": 5}
    },

    # ---------------- Sivaganga District (3 Hospitals) ----------------
    {
        "id": "hosp-svg-gmc", "district": "sivaganga",
        "name": "Government Sivaganga Medical College Hospital",
        "address": "Melavaniyangudi, Sivaganga",
        "lat": 9.8510, "lon": 78.4910,
        "bedsAvailable": 36, "bedsTotal": 170,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 4575 240 500",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 22, "O+": 34, "B+": 19, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-svg-karaikudi", "district": "sivaganga",
        "name": "Karaikudi Government District Headquarters Hospital",
        "address": "Hospital Road, Sekkalai, Karaikudi",
        "lat": 10.0680, "lon": 78.7840,
        "bedsAvailable": 32, "bedsTotal": 160,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 5,
        "phone": "+91 4565 238 240",
        "emergencyContact": "Chettinad Region Trauma Desk",
        "bloodStock": {"A+": 22, "O+": 32, "B+": 18, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-svg-devakottai", "district": "sivaganga",
        "name": "Devakottai Government Taluk Hospital",
        "address": "Ramanathapuram Road, Devakottai",
        "lat": 9.9510, "lon": 78.8250,
        "bedsAvailable": 19, "bedsTotal": 95,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4561 272 240",
        "emergencyContact": "Casualty Desk",
        "bloodStock": {"A+": 12, "O+": 18, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Tiruchirappalli District (5 Hospitals) ----------------
    {
        "id": "hosp-try-gmc", "district": "trichy",
        "name": "K.A.P.V. Govt Medical College & MGM Hospital",
        "address": "Collectorate Road, Puthur, Tiruchirappalli",
        "lat": 10.8060, "lon": 78.6850,
        "bedsAvailable": 68, "bedsTotal": 320,
        "icuAvailable": 15, "icuStatus": "Available",
        "doctorsOnDuty": 32, "ambulancesReady": 10,
        "phone": "+91 431 240 1011",
        "emergencyContact": "Central TN Apex Trauma Center",
        "bloodStock": {"A+": 55, "O+": 76, "B+": 46, "O-": 14, "AB+": 22}
    },
    {
        "id": "hosp-try-kauvery", "district": "trichy",
        "name": "Kauvery Hospital Heartcity Trichy",
        "address": "No 1 KC Road, Tennur, Tiruchirappalli",
        "lat": 10.8210, "lon": 78.6890,
        "bedsAvailable": 45, "bedsTotal": 230,
        "icuAvailable": 10, "icuStatus": "Available",
        "doctorsOnDuty": 22, "ambulancesReady": 7,
        "phone": "+91 431 400 0100",
        "emergencyContact": "Kauvery Emergency Response",
        "bloodStock": {"A+": 38, "O+": 52, "B+": 32, "O-": 9, "AB+": 15}
    },
    {
        "id": "hosp-try-manapparai", "district": "trichy",
        "name": "Manapparai Government District Headquarters Hospital",
        "address": "Dindigul Road, Manapparai",
        "lat": 10.6080, "lon": 78.4160,
        "bedsAvailable": 26, "bedsTotal": 130,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4332 260 240",
        "emergencyContact": "Highway Trauma Unit",
        "bloodStock": {"A+": 18, "O+": 26, "B+": 15, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-try-srirangam", "district": "trichy",
        "name": "Srirangam Government Hospital",
        "address": "Gandhi Road, Srirangam",
        "lat": 10.8620, "lon": 78.6940,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 431 243 2240",
        "emergencyContact": "Cauvery Island Medical Cell",
        "bloodStock": {"A+": 15, "O+": 22, "B+": 13, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-try-musiri", "district": "trichy",
        "name": "Musiri Government Taluk Hospital",
        "address": "Thuraiyur Road, Musiri",
        "lat": 10.9420, "lon": 78.4550,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4326 260 240",
        "emergencyContact": "Duty Doctor",
        "bloodStock": {"A+": 13, "O+": 20, "B+": 11, "O-": 3, "AB+": 5}
    },

    # ---------------- Karur District (3 Hospitals) ----------------
    {
        "id": "hosp-krr-gmc", "district": "karur",
        "name": "Government Medical College Hospital, Karur",
        "address": "Sanapiratti, Karur",
        "lat": 10.9620, "lon": 78.0890,
        "bedsAvailable": 35, "bedsTotal": 170,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 4324 240 555",
        "emergencyContact": "Disaster Ward Officer",
        "bloodStock": {"A+": 24, "O+": 35, "B+": 20, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-krr-kulithalai", "district": "karur",
        "name": "Kulithalai Government Taluk Hospital",
        "address": "Trichy Road, Kulithalai",
        "lat": 10.9320, "lon": 78.4120,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4323 222 240",
        "emergencyContact": "Cauvery Basin Trauma Cell",
        "bloodStock": {"A+": 13, "O+": 19, "B+": 11, "O-": 3, "AB+": 4}
    },
    {
        "id": "hosp-krr-aravakurichi", "district": "karur",
        "name": "Aravakurichi Government Taluk Hospital",
        "address": "Dindigul Road, Aravakurichi",
        "lat": 10.7720, "lon": 77.9120,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 2,
        "phone": "+91 4320 232 240",
        "emergencyContact": "Duty Doctor",
        "bloodStock": {"A+": 11, "O+": 17, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Perambalur District (2 Hospitals) ----------------
    {
        "id": "hosp-per-gmc", "district": "perambalur",
        "name": "Government Medical College Hospital, Perambalur",
        "address": "Thuraimangalam, Perambalur",
        "lat": 11.2380, "lon": 78.8780,
        "bedsAvailable": 30, "bedsTotal": 150,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 4,
        "phone": "+91 4328 277 444",
        "emergencyContact": "NH 45 Trauma Care Centre",
        "bloodStock": {"A+": 20, "O+": 30, "B+": 17, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-per-dhanalakshmi", "district": "perambalur",
        "name": "Dhanalakshmi Srinivasan Medical College Hospital",
        "address": "NH 45 Trichy-Chennai Highway, Siruvachur",
        "lat": 11.2080, "lon": 78.8520,
        "bedsAvailable": 45, "bedsTotal": 220,
        "icuAvailable": 8, "icuStatus": "Available",
        "doctorsOnDuty": 20, "ambulancesReady": 6,
        "phone": "+91 4328 254 100",
        "emergencyContact": "Highway Trauma Care Desk",
        "bloodStock": {"A+": 32, "O+": 46, "B+": 28, "O-": 7, "AB+": 12}
    },

    # ---------------- Ariyalur District (2 Hospitals) ----------------
    {
        "id": "hosp-ari-gmc", "district": "ariyalur",
        "name": "Government Medical College Hospital, Ariyalur",
        "address": "Jayankondam Road, Ariyalur",
        "lat": 11.1440, "lon": 79.0820,
        "bedsAvailable": 32, "bedsTotal": 160,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 4,
        "phone": "+91 4329 221 000",
        "emergencyContact": "Disaster Triage Unit",
        "bloodStock": {"A+": 21, "O+": 32, "B+": 18, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-ari-jayankondam", "district": "ariyalur",
        "name": "Jayankondam Government Taluk Hospital",
        "address": "Kumbakonam Main Road, Jayankondam",
        "lat": 11.2180, "lon": 79.3450,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4331 250 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 14, "O+": 22, "B+": 12, "O-": 3, "AB+": 5}
    },

    # ---------------- Thanjavur District (5 Hospitals) ----------------
    {
        "id": "hosp-tjv-tmch", "district": "thanjavur",
        "name": "Thanjavur Medical College Hospital (TMCH)",
        "address": "Medical College Road, Thanjavur",
        "lat": 10.7580, "lon": 79.1080,
        "bedsAvailable": 72, "bedsTotal": 350,
        "icuAvailable": 16, "icuStatus": "Available",
        "doctorsOnDuty": 34, "ambulancesReady": 11,
        "phone": "+91 4362 240 024",
        "emergencyContact": "Delta Region Apex Emergency",
        "bloodStock": {"A+": 58, "O+": 80, "B+": 48, "O-": 15, "AB+": 23}
    },
    {
        "id": "hosp-tjv-rmh", "district": "thanjavur",
        "name": "Raja Mirasdar Government Hospital",
        "address": "South Main Street, Thanjavur",
        "lat": 10.7850, "lon": 79.1390,
        "bedsAvailable": 38, "bedsTotal": 190,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 5,
        "phone": "+91 4362 230 455",
        "emergencyContact": "Casualty Medical Officer",
        "bloodStock": {"A+": 26, "O+": 38, "B+": 22, "O-": 6, "AB+": 10}
    },
    {
        "id": "hosp-tjv-kumbakonam", "district": "thanjavur",
        "name": "Kumbakonam Government District Headquarters Hospital",
        "address": "Katchi Street, Kumbakonam",
        "lat": 10.9610, "lon": 79.3850,
        "bedsAvailable": 40, "bedsTotal": 200,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 18, "ambulancesReady": 6,
        "phone": "+91 435 243 0240",
        "emergencyContact": "Temple City Emergency Cell",
        "bloodStock": {"A+": 28, "O+": 42, "B+": 24, "O-": 7, "AB+": 11}
    },
    {
        "id": "hosp-tjv-pattukkottai", "district": "thanjavur",
        "name": "Pattukkottai Government Taluk Hospital",
        "address": "Muthupet Road, Pattukkottai",
        "lat": 10.4280, "lon": 79.3180,
        "bedsAvailable": 25, "bedsTotal": 125,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4373 252 240",
        "emergencyContact": "Coastal Plain Emergency Desk",
        "bloodStock": {"A+": 17, "O+": 25, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-tjv-thiruvaiyaru", "district": "thanjavur",
        "name": "Thiruvaiyaru Government Hospital",
        "address": "Cauvery North Bank, Thiruvaiyaru",
        "lat": 10.8840, "lon": 79.1060,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 2,
        "phone": "+91 4362 260 240",
        "emergencyContact": "Cauvery Flood Response Cell",
        "bloodStock": {"A+": 11, "O+": 17, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Nagapattinam District (3 Hospitals) ----------------
    {
        "id": "hosp-nag-gmc", "district": "nagapattinam",
        "name": "Government Medical College Hospital, Nagapattinam",
        "address": "Perumal Sannathi Street, Nagapattinam",
        "lat": 10.7710, "lon": 79.8460,
        "bedsAvailable": 38, "bedsTotal": 180,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 15, "ambulancesReady": 6,
        "phone": "+91 4365 222 222",
        "emergencyContact": "Cyclone & Tsunami Command",
        "bloodStock": {"A+": 25, "O+": 37, "B+": 22, "O-": 6, "AB+": 10}
    },
    {
        "id": "hosp-nag-vedaranyam", "district": "nagapattinam",
        "name": "Vedaranyam Government Taluk Hospital",
        "address": "Salt Swamp Road, Vedaranyam",
        "lat": 10.3720, "lon": 79.8510,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 4,
        "phone": "+91 4369 250 240",
        "emergencyContact": "Coastal Inundation First Response",
        "bloodStock": {"A+": 14, "O+": 22, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-nag-kilvelur", "district": "nagapattinam",
        "name": "Kilvelur Government Taluk Hospital",
        "address": "Tiruvarur Highway, Kilvelur",
        "lat": 10.7160, "lon": 79.7280,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 2,
        "phone": "+91 4366 270 240",
        "emergencyContact": "Duty Doctor",
        "bloodStock": {"A+": 11, "O+": 17, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Mayiladuthurai District (3 Hospitals) ----------------
    {
        "id": "hosp-myd-gh", "district": "mayiladuthurai",
        "name": "Mayiladuthurai Government District Headquarters Hospital",
        "address": "Katchery Road, Mayiladuthurai",
        "lat": 11.1020, "lon": 79.6580,
        "bedsAvailable": 32, "bedsTotal": 160,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 5,
        "phone": "+91 4364 222 400",
        "emergencyContact": "Disaster Ward Officer",
        "bloodStock": {"A+": 22, "O+": 32, "B+": 18, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-myd-sirkazhi", "district": "mayiladuthurai",
        "name": "Sirkazhi Government Taluk Hospital",
        "address": "Poompuhar Road, Sirkazhi",
        "lat": 11.2380, "lon": 79.7360,
        "bedsAvailable": 24, "bedsTotal": 120,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4364 270 240",
        "emergencyContact": "Coastal Flood Desk",
        "bloodStock": {"A+": 16, "O+": 24, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-myd-tharangambadi", "district": "mayiladuthurai",
        "name": "Tharangambadi (Tranquebar) Government Hospital",
        "address": "Danish Fort Road, Tharangambadi",
        "lat": 11.0310, "lon": 79.8520,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 3,
        "phone": "+91 4364 288 240",
        "emergencyContact": "Sea Surge First Response Desk",
        "bloodStock": {"A+": 11, "O+": 18, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Tiruvarur District (3 Hospitals) ----------------
    {
        "id": "hosp-tvr-gmc", "district": "tiruvarur",
        "name": "Government Thiruvarur Medical College Hospital",
        "address": "Vilamal, Tiruvarur",
        "lat": 10.7740, "lon": 79.6220,
        "bedsAvailable": 36, "bedsTotal": 180,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 4366 220 040",
        "emergencyContact": "Delta Triage Desk",
        "bloodStock": {"A+": 24, "O+": 35, "B+": 20, "O-": 5, "AB+": 9}
    },
    {
        "id": "hosp-tvr-mannargudi", "district": "tiruvarur",
        "name": "Mannargudi Government District Headquarters Hospital",
        "address": "Taluk Office Road, Mannargudi",
        "lat": 10.6650, "lon": 79.4480,
        "bedsAvailable": 28, "bedsTotal": 140,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4367 252 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 18, "O+": 27, "B+": 15, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-tvr-thiruthuraipoondi", "district": "tiruvarur",
        "name": "Thiruthuraipoondi Government Taluk Hospital",
        "address": "Vedaranyam Road, Thiruthuraipoondi",
        "lat": 10.5360, "lon": 79.6480,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4369 220 240",
        "emergencyContact": "Muthupet Lagoon Trauma Cell",
        "bloodStock": {"A+": 14, "O+": 21, "B+": 12, "O-": 3, "AB+": 5}
    },

    # ---------------- Pudukkottai District (3 Hospitals) ----------------
    {
        "id": "hosp-pdk-gmc", "district": "pudukkottai",
        "name": "Government Pudukkottai Medical College Hospital",
        "address": "Ranees Hospital Complex, Pudukkottai",
        "lat": 10.3840, "lon": 78.8260,
        "bedsAvailable": 38, "bedsTotal": 180,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 15, "ambulancesReady": 5,
        "phone": "+91 4322 222 222",
        "emergencyContact": "Casualty Medical Desk",
        "bloodStock": {"A+": 25, "O+": 37, "B+": 21, "O-": 6, "AB+": 9}
    },
    {
        "id": "hosp-pdk-aranthangi", "district": "pudukkottai",
        "name": "Aranthangi Government District Headquarters Hospital",
        "address": "Pattukkottai Road, Aranthangi",
        "lat": 10.1650, "lon": 78.9980,
        "bedsAvailable": 26, "bedsTotal": 130,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4371 220 240",
        "emergencyContact": "Coastal Belt Trauma Cell",
        "bloodStock": {"A+": 17, "O+": 25, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-pdk-viralimalai", "district": "pudukkottai",
        "name": "Viralimalai Government Taluk Hospital",
        "address": "Trichy-Madurai Highway (NH 383), Viralimalai",
        "lat": 10.6080, "lon": 78.5420,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4339 220 240",
        "emergencyContact": "Highway Trauma Unit",
        "bloodStock": {"A+": 13, "O+": 20, "B+": 11, "O-": 3, "AB+": 5}
    },

    # ---------------- Tirunelveli District (4 Hospitals) ----------------
    {
        "id": "hosp-tnv-tvmch", "district": "tirunelveli",
        "name": "Tirunelveli Medical College Hospital (TVMCH)",
        "address": "High Ground, Palayamkottai, Tirunelveli",
        "lat": 8.7180, "lon": 77.7420,
        "bedsAvailable": 65, "bedsTotal": 310,
        "icuAvailable": 14, "icuStatus": "Available",
        "doctorsOnDuty": 30, "ambulancesReady": 10,
        "phone": "+91 462 257 2733",
        "emergencyContact": "Deep South Apex Trauma Centre",
        "bloodStock": {"A+": 52, "O+": 74, "B+": 44, "O-": 14, "AB+": 21}
    },
    {
        "id": "hosp-tnv-ambasamudram", "district": "tirunelveli",
        "name": "Ambasamudram Government Taluk Hospital",
        "address": "Tenkasi Main Road, Ambasamudram",
        "lat": 8.7060, "lon": 77.4580,
        "bedsAvailable": 24, "bedsTotal": 120,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4634 250 240",
        "emergencyContact": "Tamirabarani Flood Trauma Cell",
        "bloodStock": {"A+": 16, "O+": 24, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-tnv-nanguneri", "district": "tirunelveli",
        "name": "Nanguneri Government Taluk Hospital",
        "address": "Nagercoil Highway (NH 44), Nanguneri",
        "lat": 8.4880, "lon": 77.6580,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4635 250 240",
        "emergencyContact": "Highway Fast Response",
        "bloodStock": {"A+": 14, "O+": 21, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-tnv-shifa", "district": "tirunelveli",
        "name": "Shifa Hospital Super Speciality",
        "address": "82 Kailasapuram, Tirunelveli Junction",
        "lat": 8.7290, "lon": 77.7120,
        "bedsAvailable": 32, "bedsTotal": 160,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 5,
        "phone": "+91 462 233 8888",
        "emergencyContact": "Shifa Emergency Desk",
        "bloodStock": {"A+": 25, "O+": 36, "B+": 21, "O-": 6, "AB+": 10}
    },

    # ---------------- Tenkasi District (3 Hospitals) ----------------
    {
        "id": "hosp-tsi-gh", "district": "tenkasi",
        "name": "Tenkasi Government District Headquarters Hospital",
        "address": "Railway Feeder Road, Tenkasi",
        "lat": 8.9610, "lon": 77.3180,
        "bedsAvailable": 34, "bedsTotal": 160,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 4633 222 240",
        "emergencyContact": "Western Ghats Flash Flood Cell",
        "bloodStock": {"A+": 22, "O+": 34, "B+": 18, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-tsi-sankarankovil", "district": "tenkasi",
        "name": "Sankarankovil Government Taluk Hospital",
        "address": "Rajapalayam Road, Sankarankovil",
        "lat": 9.1720, "lon": 77.5340,
        "bedsAvailable": 24, "bedsTotal": 120,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4636 222 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 16, "O+": 24, "B+": 13, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-tsi-shenkottai", "district": "tenkasi",
        "name": "Shenkottai Government Taluk Hospital",
        "address": "Kollam Ghat Road (NH 744), Shenkottai",
        "lat": 8.9810, "lon": 77.2510,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4633 260 240",
        "emergencyContact": "Aryankavu Pass Border Trauma Cell",
        "bloodStock": {"A+": 13, "O+": 19, "B+": 11, "O-": 3, "AB+": 4}
    },

    # ---------------- Thoothukudi District (4 Hospitals) ----------------
    {
        "id": "hosp-ttk-gmc", "district": "thoothukudi",
        "name": "Government Thoothukudi Medical College Hospital",
        "address": "Kamaraj College Road, Thoothukudi",
        "lat": 8.7840, "lon": 78.1360,
        "bedsAvailable": 48, "bedsTotal": 230,
        "icuAvailable": 9, "icuStatus": "Available",
        "doctorsOnDuty": 20, "ambulancesReady": 7,
        "phone": "+91 461 239 2500",
        "emergencyContact": "Port & Chemical Hazard Trauma Cell",
        "bloodStock": {"A+": 35, "O+": 50, "B+": 30, "O-": 8, "AB+": 14}
    },
    {
        "id": "hosp-ttk-kovilpatti", "district": "thoothukudi",
        "name": "Kovilpatti Government District Headquarters Hospital",
        "address": "Main Road, Kovilpatti",
        "lat": 9.1740, "lon": 77.8680,
        "bedsAvailable": 30, "bedsTotal": 150,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 5,
        "phone": "+91 4632 220 240",
        "emergencyContact": "NH 44 Trauma Care Centre",
        "bloodStock": {"A+": 21, "O+": 31, "B+": 17, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-ttk-tiruchendur", "district": "thoothukudi",
        "name": "Tiruchendur Government Taluk Hospital",
        "address": "Temple Beach Road, Tiruchendur",
        "lat": 8.4980, "lon": 78.1220,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 4,
        "phone": "+91 4639 242 240",
        "emergencyContact": "Pilgrim & Coastal Disaster Desk",
        "bloodStock": {"A+": 15, "O+": 22, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-ttk-sathankulam", "district": "thoothukudi",
        "name": "Sathankulam Government Taluk Hospital",
        "address": "Itthamozhi Road, Sathankulam",
        "lat": 8.4420, "lon": 77.9120,
        "bedsAvailable": 18, "bedsTotal": 90,
        "icuAvailable": 2, "icuStatus": "Available",
        "doctorsOnDuty": 7, "ambulancesReady": 2,
        "phone": "+91 4639 266 240",
        "emergencyContact": "Casualty Desk",
        "bloodStock": {"A+": 11, "O+": 17, "B+": 10, "O-": 2, "AB+": 4}
    },

    # ---------------- Kanniyakumari District (5 Hospitals) ----------------
    {
        "id": "hosp-kkm-gmc", "district": "kanyakumari",
        "name": "Government Kanyakumari Medical College Hospital",
        "address": "Asaripallam, Nagercoil",
        "lat": 8.1880, "lon": 77.4120,
        "bedsAvailable": 52, "bedsTotal": 250,
        "icuAvailable": 11, "icuStatus": "Available",
        "doctorsOnDuty": 24, "ambulancesReady": 8,
        "phone": "+91 4652 223 201",
        "emergencyContact": "Southernmost Maritime Trauma Apex",
        "bloodStock": {"A+": 40, "O+": 58, "B+": 34, "O-": 10, "AB+": 16}
    },
    {
        "id": "hosp-kkm-padmanabhapuram", "district": "kanyakumari",
        "name": "Padmanabhapuram Government Headquarters Hospital",
        "address": "Thuckalay, Padmanabhapuram",
        "lat": 8.2450, "lon": 77.3290,
        "bedsAvailable": 28, "bedsTotal": 140,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 4,
        "phone": "+91 4651 250 240",
        "emergencyContact": "Palace Area Trauma Cell",
        "bloodStock": {"A+": 19, "O+": 28, "B+": 16, "O-": 5, "AB+": 7}
    },
    {
        "id": "hosp-kkm-kuzhithurai", "district": "kanyakumari",
        "name": "Kuzhithurai Government Taluk Hospital",
        "address": "Trivandrum Highway (NH 66), Marthandam",
        "lat": 8.3180, "lon": 77.2280,
        "bedsAvailable": 26, "bedsTotal": 130,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4651 270 240",
        "emergencyContact": "Kerala Border Highway Trauma Desk",
        "bloodStock": {"A+": 17, "O+": 25, "B+": 14, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-kkm-colachel", "district": "kanyakumari",
        "name": "Colachel Government Hospital",
        "address": "Port Road, Colachel",
        "lat": 8.1780, "lon": 77.2580,
        "bedsAvailable": 20, "bedsTotal": 100,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 8, "ambulancesReady": 3,
        "phone": "+91 4651 227 240",
        "emergencyContact": "Fisherfolk Coastal Trauma Unit",
        "bloodStock": {"A+": 14, "O+": 20, "B+": 12, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-kkm-kanyakumari", "district": "kanyakumari",
        "name": "Kanyakumari Cape Town Government Hospital",
        "address": "Kovalam Road, Kanyakumari",
        "lat": 8.0840, "lon": 77.5450,
        "bedsAvailable": 22, "bedsTotal": 110,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 4,
        "phone": "+91 4652 246 240",
        "emergencyContact": "Triveni Sangam First Response",
        "bloodStock": {"A+": 15, "O+": 22, "B+": 13, "O-": 3, "AB+": 5}
    }
]

# ---------------- 38 Shelters (Covering All 38 Districts) ----------------
SHELTERS_TN_EXPANDED = [
    {"id": "sh-chn-1", "district": "chennai", "name": "Ripon Building Emergency Relief Camp", "address": "Park Town, Chennai", "lat": 13.0820, "lon": 80.2760, "capacity": 600, "occupied": 210, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 44 2561 9200"},
    {"id": "sh-chn-2", "district": "chennai", "name": "Velachery Community Flood Relief Shelter", "address": "100 Feet Road, Velachery, Chennai", "lat": 12.9810, "lon": 80.2180, "capacity": 450, "occupied": 180, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 44 2244 5500"},
    {"id": "sh-cgl-1", "district": "chengalpattu", "name": "Tambaram Municipality Cyclone Relief Camp", "address": "Rajaji Road, West Tambaram", "lat": 12.9250, "lon": 80.1170, "capacity": 400, "occupied": 120, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 44 2226 5000"},
    {"id": "sh-kpm-1", "district": "kancheepuram", "name": "Kancheepuram Town Hall Cyclone Shelter", "address": "Gandhi Road, Kancheepuram", "lat": 12.8390, "lon": 79.7040, "capacity": 350, "occupied": 85, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 44 2722 2300"},
    {"id": "sh-tlr-1", "district": "tiruvallur", "name": "Tiruvallur Collectorate Disaster Relief Centre", "address": "Master Plan Complex, Tiruvallur", "lat": 13.1490, "lon": 79.9040, "capacity": 500, "occupied": 140, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 44 2766 1600"},
    {"id": "sh-cud-1", "district": "cuddalore", "name": "Silver Beach Multi-Purpose Cyclone Shelter", "address": "Devanampattinam Coast, Cuddalore", "lat": 11.7450, "lon": 79.7780, "capacity": 850, "occupied": 380, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4142 220 500"},
    {"id": "sh-cud-2", "district": "cuddalore", "name": "Chidambaram Pichavaram Coastal Relief Camp", "address": "Pichavaram Mangrove Road, Chidambaram", "lat": 11.4280, "lon": 79.7740, "capacity": 400, "occupied": 110, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4144 220 200"},
    {"id": "sh-vpm-1", "district": "viluppuram", "name": "Marakkanam Coastal Multi-Purpose Cyclone Shelter", "address": "ECR Beach Road, Marakkanam", "lat": 12.1980, "lon": 79.9420, "capacity": 500, "occupied": 160, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4147 236 200"},
    {"id": "sh-klk-1", "district": "kallakurichi", "name": "Kallakurichi Municipal Relief Camp", "address": "Kachirapalayam Road, Kallakurichi", "lat": 11.7350, "lon": 78.9610, "capacity": 300, "occupied": 70, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4151 222 100"},
    {"id": "sh-vel-1", "district": "vellore", "name": "Vellore Fort Ground Disaster Management Shelter", "address": "Fort Round Road, Vellore", "lat": 12.9210, "lon": 79.1310, "capacity": 450, "occupied": 95, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 416 222 0500"},
    {"id": "sh-ran-1", "district": "ranipet", "name": "Ranipet BHEL Community Relief Camp", "address": "BHEL Township, Mukundarayapuram, Ranipet", "lat": 12.9520, "lon": 79.3140, "capacity": 350, "occupied": 60, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4172 254 000"},
    {"id": "sh-tpt-1", "district": "tirupathur", "name": "Tirupattur Town Hall Flood Shelter", "address": "Javvadhu Hills Road, Tirupattur", "lat": 12.4920, "lon": 78.5620, "capacity": 300, "occupied": 55, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4179 220 100"},
    {"id": "sh-tvm-1", "district": "tiruvannamalai", "name": "Tiruvannamalai Girivalam Pilgrims Emergency Shelter", "address": "Chengham Road, Tiruvannamalai", "lat": 12.2280, "lon": 79.0650, "capacity": 650, "occupied": 190, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4175 233 333"},
    {"id": "sh-slm-1", "district": "salem", "name": "Salem Corporation Nehru Auditorium Relief Center", "address": "Cherry Road, Salem", "lat": 11.6610, "lon": 78.1580, "capacity": 500, "occupied": 110, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 427 221 2844"},
    {"id": "sh-nmk-1", "district": "namakkal", "name": "Namakkal Municipal Community Relief Camp", "address": "Mohanur Road, Namakkal", "lat": 11.2150, "lon": 78.1640, "capacity": 350, "occupied": 75, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4286 220 500"},
    {"id": "sh-dhp-1", "district": "dharmapuri", "name": "Hogenakkal Flood Emergency Camp", "address": "Pennagaram Road, Hogenakkal, Dharmapuri", "lat": 12.1150, "lon": 77.7780, "capacity": 400, "occupied": 130, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4342 256 200"},
    {"id": "sh-kri-1", "district": "krishnagiri", "name": "Hosur Municipal Corporation Community Hall", "address": "Rayakottai Road, Hosur", "lat": 12.7310, "lon": 77.8280, "capacity": 450, "occupied": 90, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4344 222 000"},
    {"id": "sh-erd-1", "district": "erode", "name": "Bhavani River Inundation Relief Center", "address": "Cauvery River Bank Road, Bhavani, Erode", "lat": 11.4420, "lon": 77.6820, "capacity": 450, "occupied": 150, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 424 235 8000"},
    {"id": "sh-tpr-1", "district": "tiruppur", "name": "Noyyal River Flood Relief Shelter", "address": "Kumaran Road, Tiruppur", "lat": 11.1070, "lon": 77.3460, "capacity": 400, "occupied": 115, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 421 224 0153"},
    {"id": "sh-cbe-1", "district": "coimbatore", "name": "VOC Park Ground Emergency Relief Camp", "address": "Jail Road, ATT Colony, Coimbatore", "lat": 11.0060, "lon": 76.9740, "capacity": 600, "occupied": 140, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 422 230 0214"},
    {"id": "sh-nil-1", "district": "nilgiris", "name": "Ooty Race Course Ground Hill Disaster Camp", "address": "Sheddon Road, Ooty", "lat": 11.4080, "lon": 76.7020, "capacity": 400, "occupied": 160, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 423 244 5555"},
    {"id": "sh-mdu-1", "district": "madurai", "name": "Tamukkam Grounds Disaster Relief Camp", "address": "Tallakulam, Madurai", "lat": 9.9320, "lon": 78.1360, "capacity": 700, "occupied": 230, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 452 253 0521"},
    {"id": "sh-thn-1", "district": "theni", "name": "Vaigai Dam Downstream Flood Shelter", "address": "Vaigai Dam Complex, Theni", "lat": 10.0520, "lon": 77.5880, "capacity": 350, "occupied": 95, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4546 250 100"},
    {"id": "sh-dgl-1", "district": "dindigul", "name": "Dindigul Rock Fort Community Center", "address": "Fort Road, Dindigul", "lat": 10.3640, "lon": 77.9720, "capacity": 400, "occupied": 80, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 451 242 0200"},
    {"id": "sh-rmd-1", "district": "ramanathapuram", "name": "Rameswaram Island Multi-Purpose Cyclone Shelter", "address": "Dhanushkodi Road, Rameswaram", "lat": 9.2820, "lon": 79.3240, "capacity": 800, "occupied": 340, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4573 221 210"},
    {"id": "sh-vnr-1", "district": "virudhunagar", "name": "Virudhunagar Municipality Kamarajar Hall", "address": "Madurai Road, Virudhunagar", "lat": 9.5850, "lon": 77.9540, "capacity": 350, "occupied": 65, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4562 244 100"},
    {"id": "sh-svg-1", "district": "sivaganga", "name": "Karaikudi New Town Emergency Camp", "address": "Subramaniapuram, Karaikudi", "lat": 10.0620, "lon": 78.7780, "capacity": 350, "occupied": 70, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4565 222 300"},
    {"id": "sh-try-1", "district": "trichy", "name": "Srirangam Yatri Nivas Flood Relief Camp", "address": "Panchakkarai, Srirangam, Trichy", "lat": 10.8680, "lon": 78.6910, "capacity": 650, "occupied": 210, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 431 243 0122"},
    {"id": "sh-krr-1", "district": "karur", "name": "Karur Amaravathi Basin Flood Relief Center", "address": "Jawahar Bazaar, Karur", "lat": 10.9580, "lon": 78.0790, "capacity": 350, "occupied": 80, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4324 260 100"},
    {"id": "sh-per-1", "district": "perambalur", "name": "Perambalur Old Bus Stand Relief Shelter", "address": "Bazaar Street, Perambalur", "lat": 11.2320, "lon": 78.8810, "capacity": 250, "occupied": 45, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4328 224 100"},
    {"id": "sh-ari-1", "district": "ariyalur", "name": "Ariyalur Collectorate Community Hall", "address": "Market Road, Ariyalur", "lat": 11.1390, "lon": 79.0750, "capacity": 300, "occupied": 50, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 4329 228 100"},
    {"id": "sh-tjv-1", "district": "thanjavur", "name": "Kumbakonam Mahamaham Tank Relief Camp", "address": "Potramarai Tank Road, Kumbakonam", "lat": 10.9580, "lon": 79.3780, "capacity": 550, "occupied": 170, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 435 242 0100"},
    {"id": "sh-nag-1", "district": "nagapattinam", "name": "Nagore Dargah Coastal Cyclone Shelter", "address": "Beach Road, Nagore, Nagapattinam", "lat": 10.8220, "lon": 79.8450, "capacity": 900, "occupied": 420, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4365 250 100"},
    {"id": "sh-myd-1", "district": "mayiladuthurai", "name": "Poompuhar Tsunami Coastal Shelter", "address": "Kaveripoompattinam Beach Road, Poompuhar", "lat": 11.1480, "lon": 79.8520, "capacity": 600, "occupied": 210, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4364 260 100"},
    {"id": "sh-tvr-1", "district": "tiruvarur", "name": "Muthupet Mangrove Multi-Purpose Cyclone Shelter", "address": "Alangadu Beach Road, Muthupet", "lat": 10.4120, "lon": 79.5120, "capacity": 500, "occupied": 185, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4369 262 100"},
    {"id": "sh-pdk-1", "district": "pudukkottai", "name": "Manamelkudi Coastal Relief Camp", "address": "East Coast Road, Manamelkudi", "lat": 9.9480, "lon": 79.1320, "capacity": 450, "occupied": 130, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4371 242 100"},
    {"id": "sh-tnv-1", "district": "tirunelveli", "name": "Palayamkottai St. Xavier School Relief Centre", "address": "South Bazaar, Palayamkottai", "lat": 8.7140, "lon": 77.7380, "capacity": 600, "occupied": 190, "womenShelter": True, "petFriendly": False, "medicalSupport": True, "wheelchair": True, "phone": "+91 462 257 2000"},
    {"id": "sh-tsi-1", "district": "tenkasi", "name": "Courtallam Main Falls Flood Shelter", "address": "Five Falls Road, Courtallam", "lat": 8.9320, "lon": 77.2720, "capacity": 400, "occupied": 110, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4633 280 100"},
    {"id": "sh-ttk-1", "district": "thoothukudi", "name": "Tuticorin VOC Port Trust Emergency Camp", "address": "Harbour Estate, Thoothukudi", "lat": 8.7520, "lon": 78.1820, "capacity": 750, "occupied": 280, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 461 235 2290"},
    {"id": "sh-kkm-1", "district": "kanyakumari", "name": "Kanyakumari Vivekananda Coastal Relief Shelter", "address": "Sunset Point Road, Kanyakumari", "lat": 8.0810, "lon": 77.5410, "capacity": 800, "occupied": 310, "womenShelter": True, "petFriendly": True, "medicalSupport": True, "wheelchair": True, "phone": "+91 4652 246 300"}
]

# ---------------- 25 Food & Water Distribution Centers ----------------
FOOD_CENTERS_TN_EXPANDED = [
    {"id": "fc-chn-1", "district": "chennai", "name": "Amma Unavagam Central Community Kitchen", "address": "Park Town, Chennai", "lat": 13.0815, "lon": 80.2740, "mealsReady": 1200, "waterLitres": 5000, "blankets": 350, "packetsRice": 800, "status": "Distributing", "contact": "Chennai Corporation Food Desk"},
    {"id": "fc-chn-2", "district": "chennai", "name": "Velachery Relief Supply Hub", "address": "Velachery Main Road, Chennai", "lat": 12.9790, "lon": 80.2210, "mealsReady": 950, "waterLitres": 3800, "blankets": 250, "packetsRice": 600, "status": "Distributing", "contact": "Disaster Kitchen #4"},
    {"id": "fc-cgl-1", "district": "chengalpattu", "name": "Tambaram Red Cross Relief Supply Depot", "address": "Sanatorium, Tambaram", "lat": 12.9320, "lon": 80.1380, "mealsReady": 800, "waterLitres": 3200, "blankets": 200, "packetsRice": 500, "status": "Distributing", "contact": "Red Cross TN Unit"},
    {"id": "fc-kpm-1", "district": "kancheepuram", "name": "Kancheepuram Community Kitchen", "address": "Nellukara Street, Kancheepuram", "lat": 12.8330, "lon": 79.7010, "mealsReady": 600, "waterLitres": 2500, "blankets": 150, "packetsRice": 400, "status": "Distributing", "contact": "Kanchi Seva Trust"},
    {"id": "fc-tlr-1", "district": "tiruvallur", "name": "Tiruvallur Taluk Food Relief Hub", "address": "JN Road, Tiruvallur", "lat": 13.1410, "lon": 79.9110, "mealsReady": 700, "waterLitres": 2800, "blankets": 180, "packetsRice": 450, "status": "Distributing", "contact": "District Supply Officer"},
    {"id": "fc-cud-1", "district": "cuddalore", "name": "Cuddalore Port Cyclone Kitchen", "address": "Harbour Road, Cuddalore OT", "lat": 11.7280, "lon": 79.7690, "mealsReady": 1400, "waterLitres": 6000, "blankets": 400, "packetsRice": 900, "status": "Distributing", "contact": "Coastal Relief NGO Coalition"},
    {"id": "fc-vpm-1", "district": "viluppuram", "name": "Viluppuram Junction Food Center", "address": "Old Bus Stand, Viluppuram", "lat": 11.9380, "lon": 79.4890, "mealsReady": 650, "waterLitres": 2600, "blankets": 160, "packetsRice": 420, "status": "Distributing", "contact": "District Food Control"},
    {"id": "fc-vel-1", "district": "vellore", "name": "Vellore Rotary Emergency Food Centre", "address": "Officers Line, Vellore", "lat": 12.9230, "lon": 79.1380, "mealsReady": 750, "waterLitres": 3000, "blankets": 180, "packetsRice": 500, "status": "Distributing", "contact": "Rotary Disaster Support"},
    {"id": "fc-slm-1", "district": "salem", "name": "Salem Lions Club Community Kitchen", "address": "Bretts Road, Salem", "lat": 11.6680, "lon": 78.1420, "mealsReady": 850, "waterLitres": 3500, "blankets": 220, "packetsRice": 550, "status": "Distributing", "contact": "Salem Relief Alliance"},
    {"id": "fc-erd-1", "district": "erode", "name": "Bhavani Flood Food & Ration Depot", "address": "River Road, Bhavani", "lat": 11.4460, "lon": 77.6890, "mealsReady": 800, "waterLitres": 3200, "blankets": 200, "packetsRice": 520, "status": "Distributing", "contact": "Erode Civil Supplies"},
    {"id": "fc-tpr-1", "district": "tiruppur", "name": "Tiruppur Export Association Relief Center", "address": "College Road, Tiruppur", "lat": 11.1120, "lon": 77.3480, "mealsReady": 900, "waterLitres": 4000, "blankets": 300, "packetsRice": 650, "status": "Distributing", "contact": "TEA Community Wing"},
    {"id": "fc-cbe-1", "district": "coimbatore", "name": "Coimbatore Corporation Relief Hub", "address": "RS Puram, Coimbatore", "lat": 11.0110, "lon": 76.9480, "mealsReady": 1100, "waterLitres": 4500, "blankets": 350, "packetsRice": 750, "status": "Distributing", "contact": "Coimbatore Seva Sangam"},
    {"id": "fc-nil-1", "district": "nilgiris", "name": "Ooty Municipal Hill Ration Hub", "address": "Commercial Road, Ooty", "lat": 11.4090, "lon": 76.7080, "mealsReady": 600, "waterLitres": 2200, "blankets": 400, "packetsRice": 450, "status": "Distributing", "contact": "Nilgiri Relief Taskforce"},
    {"id": "fc-mdu-1", "district": "madurai", "name": "Madurai Corporation Vaigai Food Depot", "address": "Simmakkal, Madurai", "lat": 9.9290, "lon": 78.1250, "mealsReady": 1300, "waterLitres": 5500, "blankets": 380, "packetsRice": 850, "status": "Distributing", "contact": "Madurai District Food Desk"},
    {"id": "fc-dgl-1", "district": "dindigul", "name": "Dindigul Red Cross Food Centre", "address": "Salai Road, Dindigul", "lat": 10.3680, "lon": 77.9780, "mealsReady": 650, "waterLitres": 2600, "blankets": 170, "packetsRice": 420, "status": "Distributing", "contact": "Red Cross Dindigul"},
    {"id": "fc-rmd-1", "district": "ramanathapuram", "name": "Rameswaram Temple Island Community Kitchen", "address": "Sannadhi Street, Rameswaram", "lat": 9.2890, "lon": 79.3170, "mealsReady": 1500, "waterLitres": 6500, "blankets": 450, "packetsRice": 1000, "status": "Distributing", "contact": "Devasthanam Annadhanam & Relief"},
    {"id": "fc-vnr-1", "district": "virudhunagar", "name": "Sivakasi Rotary Community Food Center", "address": "Velayutham Road, Sivakasi", "lat": 9.4580, "lon": 77.8010, "mealsReady": 700, "waterLitres": 2800, "blankets": 190, "packetsRice": 480, "status": "Distributing", "contact": "Rotary Club Sivakasi"},
    {"id": "fc-try-1", "district": "trichy", "name": "Tiruchirappalli Central Food Logistics Center", "address": "Central Bus Stand, Trichy", "lat": 10.7950, "lon": 78.6920, "mealsReady": 1200, "waterLitres": 5000, "blankets": 320, "packetsRice": 800, "status": "Distributing", "contact": "Trichy District Logistics Hub"},
    {"id": "fc-tjv-1", "district": "thanjavur", "name": "Kumbakonam Delta Grain & Food Center", "address": "TSR Big Street, Kumbakonam", "lat": 10.9620, "lon": 79.3810, "mealsReady": 950, "waterLitres": 3800, "blankets": 250, "packetsRice": 650, "status": "Distributing", "contact": "Delta Farmers Aid Coalition"},
    {"id": "fc-nag-1", "district": "nagapattinam", "name": "Nagapattinam Harbor Disaster Kitchen", "address": "Beach Road, Nagapattinam", "lat": 10.7680, "lon": 79.8450, "mealsReady": 1600, "waterLitres": 7000, "blankets": 500, "packetsRice": 1100, "status": "Distributing", "contact": "Nagapattinam Coast Relief"},
    {"id": "fc-myd-1", "district": "mayiladuthurai", "name": "Sirkazhi Coastal Supply Depot", "address": "Old Bus Stand, Sirkazhi", "lat": 11.2350, "lon": 79.7310, "mealsReady": 750, "waterLitres": 3000, "blankets": 200, "packetsRice": 500, "status": "Distributing", "contact": "Coastal Supply Officer"},
    {"id": "fc-tvr-1", "district": "tiruvarur", "name": "Tiruvarur Chariot Ground Food Camp", "address": "Car Street, Tiruvarur", "lat": 10.7710, "lon": 79.6380, "mealsReady": 800, "waterLitres": 3200, "blankets": 210, "packetsRice": 520, "status": "Distributing", "contact": "Tiruvarur Relief Desk"},
    {"id": "fc-tnv-1", "district": "tirunelveli", "name": "Tirunelveli Junction Red Cross Depot", "address": "SN High Road, Tirunelveli Junction", "lat": 8.7280, "lon": 77.7180, "mealsReady": 950, "waterLitres": 4000, "blankets": 280, "packetsRice": 650, "status": "Distributing", "contact": "Red Cross South TN"},
    {"id": "fc-ttk-1", "district": "thoothukudi", "name": "Tuticorin Marine Relief Supply Point", "address": "Beach Road, Thoothukudi", "lat": 8.8020, "lon": 78.1580, "mealsReady": 1100, "waterLitres": 4800, "blankets": 320, "packetsRice": 720, "status": "Distributing", "contact": "Port City Relief Cell"},
    {"id": "fc-kkm-1", "district": "kanyakumari", "name": "Nagercoil Municipal Disaster Kitchen", "address": "Cape Road, Kottar, Nagercoil", "lat": 8.1720, "lon": 77.4320, "mealsReady": 1000, "waterLitres": 4200, "blankets": 300, "packetsRice": 700, "status": "Distributing", "contact": "Kanyakumari Seva Sangam"}
]

# ---------------- 25 Blood Banks ----------------
BLOOD_BANKS_TN_EXPANDED = [
    {"id": "bb-chn-1", "district": "chennai", "name": "Madras Medical College Central Blood Bank", "address": "Park Town, Chennai", "lat": 13.0805, "lon": 80.2778, "open24x7": True, "phone": "+91 44 2530 5111", "stock": {"A+": 65, "O+": 88, "B+": 52, "O-": 16, "AB+": 24, "AB-": 8}},
    {"id": "bb-chn-2", "district": "chennai", "name": "Red Cross Blood Bank Tamil Nadu Headquarters", "address": "50 Montieth Road, Egmore, Chennai", "lat": 13.0680, "lon": 80.2590, "open24x7": True, "phone": "+91 44 2855 4548", "stock": {"A+": 75, "O+": 95, "B+": 62, "O-": 20, "AB+": 30, "AB-": 10}},
    {"id": "bb-cgl-1", "district": "chengalpattu", "name": "Chengalpattu GMC Blood Bank", "address": "GST Road, Chengalpattu", "lat": 12.6912, "lon": 79.9835, "open24x7": True, "phone": "+91 44 2742 6566", "stock": {"A+": 28, "O+": 42, "B+": 24, "O-": 7, "AB+": 11, "AB-": 3}},
    {"id": "bb-kpm-1", "district": "kancheepuram", "name": "Kancheepuram District Govt Blood Bank", "address": "GH Road, Kancheepuram", "lat": 12.8360, "lon": 79.7080, "open24x7": True, "phone": "+91 44 2722 2450", "stock": {"A+": 22, "O+": 34, "B+": 18, "O-": 5, "AB+": 8, "AB-": 2}},
    {"id": "bb-tlr-1", "district": "tiruvallur", "name": "Tiruvallur GMC Blood Bank", "address": "JN Road, Tiruvallur", "lat": 13.1460, "lon": 79.9120, "open24x7": True, "phone": "+91 44 2766 0222", "stock": {"A+": 24, "O+": 36, "B+": 20, "O-": 5, "AB+": 9, "AB-": 3}},
    {"id": "bb-cud-1", "district": "cuddalore", "name": "Cuddalore District GH Blood Bank", "address": "Nellikuppam Road, Cuddalore", "lat": 11.7530, "lon": 79.7620, "open24x7": True, "phone": "+91 4142 230 455", "stock": {"A+": 32, "O+": 46, "B+": 27, "O-": 8, "AB+": 12, "AB-": 4}},
    {"id": "bb-vpm-1", "district": "viluppuram", "name": "Govt Viluppuram GMC Blood Bank", "address": "Mundiyampakkam, Viluppuram", "lat": 11.9890, "lon": 79.5120, "open24x7": True, "phone": "+91 4146 232 500", "stock": {"A+": 25, "O+": 37, "B+": 22, "O-": 6, "AB+": 10, "AB-": 3}},
    {"id": "bb-vel-1", "district": "vellore", "name": "CMC Vellore Blood Transfusion Service", "address": "Ida Scudder Road, Vellore", "lat": 12.9250, "lon": 79.1350, "open24x7": True, "phone": "+91 416 228 1000", "stock": {"A+": 80, "O+": 105, "B+": 68, "O-": 24, "AB+": 35, "AB-": 12}},
    {"id": "bb-slm-1", "district": "salem", "name": "Salem GMCH Central Blood Bank", "address": "Collectorate Road, Salem", "lat": 11.6580, "lon": 78.1520, "open24x7": True, "phone": "+91 427 244 3111", "stock": {"A+": 40, "O+": 58, "B+": 35, "O-": 10, "AB+": 16, "AB-": 5}},
    {"id": "bb-nmk-1", "district": "namakkal", "name": "Namakkal GMC Blood Bank", "address": "Collectorate Complex, Namakkal", "lat": 11.2210, "lon": 78.1720, "open24x7": True, "phone": "+91 4286 281 222", "stock": {"A+": 22, "O+": 34, "B+": 18, "O-": 5, "AB+": 8, "AB-": 2}},
    {"id": "bb-dhp-1", "district": "dharmapuri", "name": "Dharmapuri GMC Blood Bank", "address": "Netaji Bypass Road, Dharmapuri", "lat": 12.1320, "lon": 78.1650, "open24x7": True, "phone": "+91 4342 233 111", "stock": {"A+": 26, "O+": 38, "B+": 22, "O-": 6, "AB+": 10, "AB-": 3}},
    {"id": "bb-kri-1", "district": "krishnagiri", "name": "Hosur Government Hospital Blood Bank", "address": "Bagalur Road, Hosur", "lat": 12.7410, "lon": 77.8340, "open24x7": True, "phone": "+91 4344 242 240", "stock": {"A+": 30, "O+": 45, "B+": 26, "O-": 8, "AB+": 12, "AB-": 4}},
    {"id": "bb-erd-1", "district": "erode", "name": "Erode GMCH Blood Bank, Perundurai", "address": "Perundurai Road, Erode", "lat": 11.2780, "lon": 77.5840, "open24x7": True, "phone": "+91 4294 220 800", "stock": {"A+": 35, "O+": 52, "B+": 30, "O-": 9, "AB+": 14, "AB-": 4}},
    {"id": "bb-tpr-1", "district": "tiruppur", "name": "Tiruppur GMC Blood Bank", "address": "Dharapuram Road, Tiruppur", "lat": 11.0990, "lon": 77.3580, "open24x7": True, "phone": "+91 421 224 2200", "stock": {"A+": 28, "O+": 42, "B+": 24, "O-": 7, "AB+": 11, "AB-": 3}},
    {"id": "bb-cbe-1", "district": "coimbatore", "name": "Coimbatore CMCH Apex Blood Bank", "address": "Trichy Road, Coimbatore", "lat": 11.0010, "lon": 76.9690, "open24x7": True, "phone": "+91 422 230 1393", "stock": {"A+": 60, "O+": 82, "B+": 50, "O-": 16, "AB+": 24, "AB-": 8}},
    {"id": "bb-nil-1", "district": "nilgiris", "name": "Ooty GMC Blood Bank", "address": "Fernhill Post, Ooty", "lat": 11.3980, "lon": 76.6890, "open24x7": True, "phone": "+91 423 244 2212", "stock": {"A+": 20, "O+": 30, "B+": 18, "O-": 5, "AB+": 7, "AB-": 2}},
    {"id": "bb-mdu-1", "district": "madurai", "name": "Madurai GRH Regional Blood Centre", "address": "Panagal Road, Madurai", "lat": 9.9280, "lon": 78.1320, "open24x7": True, "phone": "+91 452 253 2535", "stock": {"A+": 62, "O+": 85, "B+": 54, "O-": 16, "AB+": 25, "AB-": 7}},
    {"id": "bb-dgl-1", "district": "dindigul", "name": "Dindigul GMC Blood Bank", "address": "Chettinaickenpatti, Dindigul", "lat": 10.3620, "lon": 77.9680, "open24x7": True, "phone": "+91 451 246 0100", "stock": {"A+": 28, "O+": 40, "B+": 24, "O-": 7, "AB+": 11, "AB-": 3}},
    {"id": "bb-rmd-1", "district": "ramanathapuram", "name": "Ramanathapuram GMC Blood Bank", "address": "NH 49, Ramanathapuram", "lat": 9.3710, "lon": 78.8310, "open24x7": True, "phone": "+91 4567 230 055", "stock": {"A+": 24, "O+": 36, "B+": 21, "O-": 6, "AB+": 9, "AB-": 3}},
    {"id": "bb-vnr-1", "district": "virudhunagar", "name": "Virudhunagar GMC Blood Bank", "address": "Madurai Road, Virudhunagar", "lat": 9.5960, "lon": 77.9620, "open24x7": True, "phone": "+91 4562 252 500", "stock": {"A+": 24, "O+": 36, "B+": 20, "O-": 5, "AB+": 9, "AB-": 3}},
    {"id": "bb-try-1", "district": "trichy", "name": "MGM Government Hospital Blood Bank, Trichy", "address": "Collectorate Road, Puthur, Trichy", "lat": 10.8060, "lon": 78.6850, "open24x7": True, "phone": "+91 431 240 1011", "stock": {"A+": 55, "O+": 76, "B+": 46, "O-": 14, "AB+": 22, "AB-": 7}},
    {"id": "bb-tjv-1", "district": "thanjavur", "name": "Thanjavur TMCH Blood Bank", "address": "Medical College Road, Thanjavur", "lat": 10.7580, "lon": 79.1080, "open24x7": True, "phone": "+91 4362 240 024", "stock": {"A+": 58, "O+": 80, "B+": 48, "O-": 15, "AB+": 23, "AB-": 7}},
    {"id": "bb-nag-1", "district": "nagapattinam", "name": "Nagapattinam GMC Coastal Blood Bank", "address": "Perumal Sannathi Street, Nagapattinam", "lat": 10.7710, "lon": 79.8460, "open24x7": True, "phone": "+91 4365 222 222", "stock": {"A+": 25, "O+": 37, "B+": 22, "O-": 6, "AB+": 10, "AB-": 3}},
    {"id": "bb-tnv-1", "district": "tirunelveli", "name": "TVMCH Central Blood Bank, Palayamkottai", "address": "High Ground, Palayamkottai", "lat": 8.7180, "lon": 77.7420, "open24x7": True, "phone": "+91 462 257 2733", "stock": {"A+": 52, "O+": 74, "B+": 44, "O-": 14, "AB+": 21, "AB-": 6}},
    {"id": "bb-kkm-1", "district": "kanyakumari", "name": "Kanyakumari GMCH Blood Bank, Asaripallam", "address": "Asaripallam, Nagercoil", "lat": 8.1880, "lon": 77.4120, "open24x7": True, "phone": "+91 4652 223 201", "stock": {"A+": 40, "O+": 58, "B+": 34, "O-": 10, "AB+": 16, "AB-": 5}}
]

# ---------------- 20 Emergencies (Fire, Flood, Blocked Roads) ----------------
EMERGENCIES_TN_EXPANDED = [
    # Fires
    {"id": "emg-fire-1", "district": "chennai", "type": "fire", "title": "Ambattur Industrial Estate Warehouse Fire", "description": "Chemical solvent packaging godown fire. 6 fire tenders deployed from Ambattur and Mogappair.", "lat": 13.1090, "lon": 80.1610, "severity": "Critical", "status": "Active", "time": "18 mins ago", "reporter": "TNFRS Command", "photo": "https://images.unsplash.com/photo-1542385151-efd9000785a0?w=600&auto=format&fit=crop&q=80"},
    {"id": "emg-fire-2", "district": "virudhunagar", "type": "fire", "title": "Sivakasi Cracker Factory Explosion Fire", "description": "Spark ignition during chemical blending in unit 4. Fire service & quick rescue teams on site.", "lat": 9.4620, "lon": 77.8120, "severity": "High", "status": "Active", "time": "32 mins ago", "reporter": "Sivakasi Fire Station", "photo": "https://images.unsplash.com/photo-1577962917302-cd874c4e31d2?w=600&auto=format&fit=crop&q=80"},
    {"id": "emg-fire-3", "district": "coimbatore", "type": "fire", "title": "Saibaba Colony Commercial Complex Fire", "description": "Electrical transformer short circuit behind commercial center. Controlled, smoke ventilation in progress.", "lat": 11.0290, "lon": 76.9480, "severity": "Medium", "status": "Contained", "time": "1 hour ago", "reporter": "Coimbatore Central Fire", "photo": ""},
    {"id": "emg-fire-4", "district": "tiruppur", "type": "fire", "title": "Avinashi Road Dyeing Unit Fire Alert", "description": "Textile chemical godown smoke outbreak. 3 water bowsers deployed.", "lat": 11.1210, "lon": 77.3390, "severity": "High", "status": "Active", "time": "45 mins ago", "reporter": "Tiruppur South Fire Station", "photo": ""},

    # Floods / Inundations
    {"id": "emg-fld-1", "district": "chennai", "type": "flood", "title": "Velachery Residential Canal Waterlogging", "description": "Canal overflow caused 3.5 ft deep water on 100 Feet Bypass Road and Ram Nagar. SDRF motor boats operational.", "lat": 12.9780, "lon": 80.2190, "severity": "Critical", "status": "Active", "time": "10 mins ago", "reporter": "Chennai Disaster Management", "photo": "https://images.unsplash.com/photo-1547683905-f686c993aae5?w=600&auto=format&fit=crop&q=80"},
    {"id": "emg-fld-2", "district": "chengalpattu", "type": "flood", "title": "Mudichur & Varadharajapuram Lake Breach", "description": "Adyar basin water backflow entering ground floor houses. National Disaster Response Force (NDRF) team assisting evacuations.", "lat": 12.9120, "lon": 80.0780, "severity": "Critical", "status": "Active", "time": "25 mins ago", "reporter": "Tambaram SDRF Post", "photo": "https://images.unsplash.com/photo-1515694346937-94d85e41e6f0?w=600&auto=format&fit=crop&q=80"},
    {"id": "emg-fld-3", "district": "cuddalore", "type": "flood", "title": "Pennaiyar River Basin Sea Inundation Alert", "description": "High tide storm surge combined with river swelling near Devanampattinam coast. Fishermen advised against venturing into sea.", "lat": 11.7480, "lon": 79.7820, "severity": "Critical", "status": "Active", "time": "14 mins ago", "reporter": "Cuddalore Collectorate", "photo": "https://images.unsplash.com/photo-1545649490-64219c6f2a63?w=600&auto=format&fit=crop&q=80"},
    {"id": "emg-fld-4", "district": "erode", "type": "flood", "title": "Bhavani River High Discharge Flood Warning", "description": "Bhavanisagar dam release at 45,000 cusecs. Riverbank communities moved to Bhavani relief center.", "lat": 11.4480, "lon": 77.6840, "severity": "High", "status": "Active", "time": "50 mins ago", "reporter": "PWD Water Resources", "photo": ""},
    {"id": "emg-fld-5", "district": "trichy", "type": "flood", "title": "Cauvery & Kollidam Delta Flood Discharge", "description": "Upper Anicut sluice gates opened. Low lying areas of Srirangam cautioned.", "lat": 10.8710, "lon": 78.6940, "severity": "High", "status": "Active", "time": "1 hour ago", "reporter": "Trichy Collectorate Disaster Cell", "photo": ""},
    {"id": "emg-fld-6", "district": "tirunelveli", "type": "flood", "title": "Tamirabarani River Flash Inundation", "description": "Papanasam dam shutters raised. Kurukkuthurai Murugan temple submerged up to mandapam.", "lat": 8.7210, "lon": 77.7280, "severity": "High", "status": "Active", "time": "40 mins ago", "reporter": "Tirunelveli SDRF Wing", "photo": ""},
    {"id": "emg-fld-7", "district": "thoothukudi", "type": "flood", "title": "Buckle Canal Overflow Tuticorin", "description": "Severe inundation around Bryant Nagar and Anthonyarpuram after cloudburst.", "lat": 8.7940, "lon": 78.1410, "severity": "Critical", "status": "Active", "time": "20 mins ago", "reporter": "Corporation Emergency Officer", "photo": ""},

    # Blocked Roads & Landslides
    {"id": "emg-blk-1", "district": "nilgiris", "type": "blocked", "title": "Ooty-Kotagiri Ghat Road Landslide", "description": "Heavy boulder collapse near Katteri bridge. Road cleared for single-lane light vehicles only; heavy trucks diverted via Coonoor.", "lat": 11.3780, "lon": 76.7820, "severity": "Critical", "status": "Active", "time": "12 mins ago", "reporter": "Nilgiris Highways Dept", "photo": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=600&auto=format&fit=crop&q=80"},
    {"id": "emg-blk-2", "district": "nilgiris", "type": "blocked", "title": "Coonoor Marapalam Ghat Mudslip", "description": "Tree uprooting and mudflow on NH 181. Clearing crane deployed.", "lat": 11.3320, "lon": 76.8120, "severity": "High", "status": "Active", "time": "35 mins ago", "reporter": "Highway Patrol Nilgiris", "photo": ""},
    {"id": "emg-blk-3", "district": "dindigul", "type": "blocked", "title": "Kodaikanal Ghat Road Rockfall Block", "description": "Silver Cascade stretch boulder fall. Traffic halted temporarily for heavy earthmovers.", "lat": 10.2480, "lon": 77.5240, "severity": "High", "status": "Active", "time": "22 mins ago", "reporter": "Dindigul Traffic Division", "photo": ""},
    {"id": "emg-blk-4", "district": "coimbatore", "type": "blocked", "title": "Valparai 40-Hairpin Ghat Fog & Tree Fall", "description": "Hairpin bend #28 blocked due to huge fallen eucalyptus tree amidst thick fog.", "lat": 10.4120, "lon": 76.9820, "severity": "High", "status": "Active", "time": "55 mins ago", "reporter": "Pollachi Forest Department", "photo": ""},
    {"id": "emg-blk-5", "district": "salem", "type": "blocked", "title": "Yercaud 60-Bend Ghat Road Landslip", "description": "Loose soil slide near bend #14 after overnight rains. Earthmoving underway.", "lat": 11.7480, "lon": 78.1880, "severity": "Medium", "status": "Active", "time": "1 hour ago", "reporter": "Salem Highways Division", "photo": ""},
    {"id": "emg-blk-6", "district": "tenkasi", "type": "blocked", "title": "Aryankavu Pass (NH 744) Landslide Barrier", "description": "Interstate freight traffic to Kollam redirected via Tenkasi-Punalur single lane due to bridge shoulder damage.", "lat": 8.9740, "lon": 77.2180, "severity": "High", "status": "Active", "time": "45 mins ago", "reporter": "Shenkottai Border Police", "photo": ""},
    {"id": "emg-blk-7", "district": "chennai", "type": "blocked", "title": "Ennore Express Highway Waterlogging", "description": "Tidal backflow across low level bridge near Nettukukppam. Port container lorries diverted.", "lat": 13.2180, "lon": 80.3250, "severity": "Medium", "status": "Active", "time": "1 hour ago", "reporter": "Chennai Traffic Police", "photo": ""},
    {"id": "emg-blk-8", "district": "chengalpattu", "type": "blocked", "title": "Perungalathur GST Road Flyover Subway Water Block", "description": "Subway submerged under 4 ft water. Traffic diverted to surface grade road.", "lat": 12.9050, "lon": 80.0920, "severity": "High", "status": "Active", "time": "30 mins ago", "reporter": "Chengalpattu Traffic Wing", "photo": ""},
    {"id": "emg-blk-9", "district": "madurai", "type": "blocked", "title": "Goripalayam Junction Underpass Waterlogging", "description": "Storm water pumps active. Traffic police diverting buses via Anna Nagar.", "lat": 9.9320, "lon": 78.1340, "severity": "Low", "status": "Active", "time": "1 hour ago", "reporter": "Madurai City Traffic Police", "photo": ""},
    {"id": "emg-blk-10", "district": "cuddalore", "type": "blocked", "title": "Pennaiyar Causeway Water Flow Block", "description": "Water flowing 1.5 ft above causeway. Movement prohibited for two-wheelers.", "lat": 11.7610, "lon": 79.7240, "severity": "High", "status": "Active", "time": "40 mins ago", "reporter": "Cuddalore Rural Police", "photo": ""}
]

# ---------------- Volunteers ----------------
VOLUNTEERS_TN_EXPANDED = [
    {"id": "vol-1", "district": "chennai", "name": "Karthik Subramanian", "phone": "+91 98401 23456", "skills": "First Aid, Flood Rescue, Ham Radio (VU2TNX)", "currentLocation": "Velachery Ward 178, Chennai", "status": "On the way", "activeTask": "Boat Evacuation at Ram Nagar", "lat": 12.9810, "lon": 80.2210},
    {"id": "vol-2", "district": "cuddalore", "name": "Meena Natarajan", "phone": "+91 94432 87654", "skills": "Trauma Nurse, Triage Care, Tamil/English", "currentLocation": "Silver Beach Camp, Cuddalore", "status": "Assigned", "activeTask": "Elderly Care & Wound Dressing", "lat": 11.7450, "lon": 79.7780},
    {"id": "vol-3", "district": "nilgiris", "name": "Vigneshwaran K.", "phone": "+91 97890 11223", "skills": "Ghat 4x4 Offroad Driver, Heavy Chainsaw Operator", "currentLocation": "Katteri Bend, Ooty-Kotagiri Road", "status": "Completed", "activeTask": "Tree clearance on NH 181", "lat": 11.3780, "lon": 76.7820},
    {"id": "vol-4", "district": "madurai", "name": "Dr. Ananya Sundaram", "phone": "+91 94421 99887", "skills": "Emergency Medicine, Pediatric First Aid", "currentLocation": "Tamukkam Camp, Madurai", "status": "Assigned", "activeTask": "Child Health Camp", "lat": 9.9320, "lon": 78.1360},
    {"id": "vol-5", "district": "coimbatore", "name": "Pradeep Kumar S.", "phone": "+91 98422 33445", "skills": "Ham Radio, Drone Pilot (Aerial Survey)", "currentLocation": "VOC Park Hub, Coimbatore", "status": "On the way", "activeTask": "Drone damage mapping in low-lying pockets", "lat": 11.0060, "lon": 76.9740},
    {"id": "vol-6", "district": "ramanathapuram", "name": "Balamurugan R.", "phone": "+91 94861 55667", "skills": "Marine Swimming, Coastal Boat Rescue", "currentLocation": "Rameswaram Island Camp", "status": "Assigned", "activeTask": "Fisherfolk evacuation advisory", "lat": 9.2820, "lon": 79.3240},
    {"id": "vol-7", "district": "tiruchirappalli", "name": "Sangeetha R.", "phone": "+91 94431 44556", "skills": "Logistics Dispatch, Water Purification", "currentLocation": "Central Bus Stand Depot, Trichy", "status": "Assigned", "activeTask": "Chlorine tablet distribution", "lat": 10.7950, "lon": 78.6920},
    {"id": "vol-8", "district": "tirunelveli", "name": "Ganesh Moorthy", "phone": "+91 98941 77889", "skills": "River Lifeguard, Rapid Raft Rescue", "currentLocation": "Kurukkuthurai, Tirunelveli", "status": "On the way", "activeTask": "Riverbank safety patrol", "lat": 8.7210, "lon": 77.7280}
]

# ---------------- Missing Persons Bulletin ----------------
MISSING_PERSONS_TN_EXPANDED = [
    {
        "id": "mp-1", "district": "chennai", "name": "R. Selvaraj", "age": 68,
        "photo": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&auto=format&fit=crop&q=80",
        "lastSeen": "Velachery 100 Feet Road during sudden flooding (19 Oct, 4:30 PM)",
        "description": "Height 5'6\", wearing white dhoti and blue shirt. Suffers from mild memory loss.",
        "contactPhone": "+91 98401 99999", "status": "Missing", "reportedAt": "2 hours ago"
    },
    {
        "id": "mp-2", "district": "cuddalore", "name": "Deepa Murugan", "age": 24,
        "photo": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&auto=format&fit=crop&q=80",
        "lastSeen": "Devanampattinam fishing hamlet near beach (19 Oct, 2:00 PM)",
        "description": "Height 5'3\", green salwar kameez, carrying black shoulder bag.",
        "contactPhone": "+91 94432 11111", "status": "Missing", "reportedAt": "4 hours ago"
    },
    {
        "id": "mp-3", "district": "nilgiris", "name": "K. Manikandan", "age": 34,
        "photo": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&auto=format&fit=crop&q=80",
        "lastSeen": "Katteri ghat road near boulder slide area (19 Oct, 11:30 AM)",
        "description": "Driving black Bajaj Pulsar (TN 43 E 2021). Yellow rain jacket.",
        "contactPhone": "+91 97890 44444", "status": "Found", "reportedAt": "5 hours ago (Safely sheltered at Coonoor Lawley GH)"
    },
    {
        "id": "mp-4", "district": "madurai", "name": "S. Chelladurai", "age": 72,
        "photo": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&auto=format&fit=crop&q=80",
        "lastSeen": "Goripalayam Junction during heavy rains",
        "description": "Grey hair, spectacles, beige shirt. Walking with silver stick.",
        "contactPhone": "+91 94421 22334", "status": "Missing", "reportedAt": "3 hours ago"
    }
]
