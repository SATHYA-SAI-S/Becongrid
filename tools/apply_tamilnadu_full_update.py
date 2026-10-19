"""
Comprehensive updater for ResQCommand Tamil Nadu - covering all 38 districts of Tamil Nadu.
"""
import json
import os
import re

HOSPITALS_TN_38 = [
    # Chennai Metropolitan
    {
        "id": "hosp-tn-chennai-1", "district": "chennai",
        "name": "Rajiv Gandhi Government General Hospital (RGGGH)",
        "address": "EVR Periyar Salai, Park Town, Chennai",
        "lat": 13.0805, "lon": 80.2778,
        "bedsAvailable": 78, "bedsTotal": 300,
        "icuAvailable": 14, "icuStatus": "Available",
        "doctorsOnDuty": 32, "ambulancesReady": 12,
        "phone": "+91 44 2530 5000",
        "emergencyContact": "Triage Chief (Dr. Murugesan)",
        "bloodStock": {"A+": 65, "O+": 88, "B+": 52, "O-": 16, "AB+": 24}
    },
    {
        "id": "hosp-tn-chennai-2", "district": "chennai",
        "name": "Government Stanley Medical College Hospital",
        "address": "Old Jail Road, Royapuram, Chennai",
        "lat": 13.1070, "lon": 80.2870,
        "bedsAvailable": 45, "bedsTotal": 200,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 20, "ambulancesReady": 6,
        "phone": "+91 44 2528 1351",
        "emergencyContact": "Casualty Desk",
        "bloodStock": {"A+": 34, "O+": 45, "B+": 28, "O-": 8, "AB+": 12}
    },
    {
        "id": "hosp-tn-chengalpattu", "district": "chengalpattu",
        "name": "Chengalpattu Government Medical College Hospital",
        "address": "GST Road, Melamaiyur, Chengalpattu",
        "lat": 12.6912, "lon": 79.9835,
        "bedsAvailable": 38, "bedsTotal": 180,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 44 2742 6566",
        "emergencyContact": "Trauma Emergency Ward",
        "bloodStock": {"A+": 26, "O+": 38, "B+": 22, "O-": 6, "AB+": 10}
    },
    {
        "id": "hosp-tn-kancheepuram", "district": "kancheepuram",
        "name": "Kancheepuram Govt District Headquarters Hospital",
        "address": "Railway Station Road, Kancheepuram",
        "lat": 12.8360, "lon": 79.7080,
        "bedsAvailable": 28, "bedsTotal": 150,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 44 2722 2450",
        "emergencyContact": "Disaster Duty MO",
        "bloodStock": {"A+": 18, "O+": 29, "B+": 15, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-tn-tiruvallur", "district": "tiruvallur",
        "name": "Government Medical College Hospital, Tiruvallur",
        "address": "Jawaharlal Nehru Road, Tiruvallur",
        "lat": 13.1460, "lon": 79.9120,
        "bedsAvailable": 32, "bedsTotal": 160,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 5,
        "phone": "+91 44 2766 0222",
        "emergencyContact": "Emergency Triage Unit",
        "bloodStock": {"A+": 22, "O+": 34, "B+": 19, "O-": 5, "AB+": 8}
    },

    # Northern Region
    {
        "id": "hosp-tn-cuddalore", "district": "cuddalore",
        "name": "Cuddalore Government District Headquarters Hospital",
        "address": "Nellikuppam Main Road, Cuddalore",
        "lat": 11.7530, "lon": 79.7620,
        "bedsAvailable": 42, "bedsTotal": 190,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 7,
        "phone": "+91 4142 230 455",
        "emergencyContact": "Cyclone Trauma Unit",
        "bloodStock": {"A+": 30, "O+": 42, "B+": 25, "O-": 7, "AB+": 11}
    },
    {
        "id": "hosp-tn-viluppuram", "district": "viluppuram",
        "name": "Government Viluppuram Medical College Hospital",
        "address": "Mundiyampakkam, Viluppuram",
        "lat": 11.9890, "lon": 79.5120,
        "bedsAvailable": 36, "bedsTotal": 170,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 4,
        "phone": "+91 4146 232 500",
        "emergencyContact": "Casualty Medical Officer",
        "bloodStock": {"A+": 24, "O+": 35, "B+": 20, "O-": 5, "AB+": 9}
    },
    {
        "id": "hosp-tn-kallakurichi", "district": "kallakurichi",
        "name": "Government Medical College Hospital, Kallakurichi",
        "address": "Siruvachur Road, Kallakurichi",
        "lat": 11.7410, "lon": 78.9690,
        "bedsAvailable": 25, "bedsTotal": 140,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 3,
        "phone": "+91 4151 222 344",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 15, "O+": 24, "B+": 14, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-tn-vellore", "district": "vellore",
        "name": "Christian Medical College & Hospital (CMC Vellore)",
        "address": "Ida Scudder Road, Vellore",
        "lat": 12.9250, "lon": 79.1350,
        "bedsAvailable": 85, "bedsTotal": 350,
        "icuAvailable": 18, "icuStatus": "Available",
        "doctorsOnDuty": 35, "ambulancesReady": 10,
        "phone": "+91 416 228 1000",
        "emergencyContact": "Emergency Dept Central Control",
        "bloodStock": {"A+": 75, "O+": 95, "B+": 60, "O-": 20, "AB+": 32}
    },
    {
        "id": "hosp-tn-ranipet", "district": "ranipet",
        "name": "Ranipet District Headquarters Hospital",
        "address": "MB Road, Walajapet, Ranipet",
        "lat": 12.9310, "lon": 79.3620,
        "bedsAvailable": 22, "bedsTotal": 130,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4172 232 240",
        "emergencyContact": "Disaster Ward Desk",
        "bloodStock": {"A+": 14, "O+": 21, "B+": 12, "O-": 3, "AB+": 4}
    },
    {
        "id": "hosp-tn-tirupathur", "district": "tirupathur",
        "name": "Government District Hospital, Tirupathur",
        "address": "Railway Road, Tirupathur",
        "lat": 12.4980, "lon": 78.5710,
        "bedsAvailable": 24, "bedsTotal": 135,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4179 220 234",
        "emergencyContact": "Casualty Duty Officer",
        "bloodStock": {"A+": 16, "O+": 22, "B+": 13, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-tn-tiruvannamalai", "district": "tiruvannamalai",
        "name": "Government Tiruvannamalai Medical College Hospital",
        "address": "Collectorate Road, Vengikkal, Tiruvannamalai",
        "lat": 12.2450, "lon": 79.0680,
        "bedsAvailable": 34, "bedsTotal": 165,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 4,
        "phone": "+91 4175 233 420",
        "emergencyContact": "Trauma Desk",
        "bloodStock": {"A+": 20, "O+": 31, "B+": 17, "O-": 4, "AB+": 7}
    },

    # Western (Kongu) Region
    {
        "id": "hosp-tn-coimbatore", "district": "coimbatore",
        "name": "Coimbatore Medical College Hospital (CMCH)",
        "address": "Trichy Road, Coimbatore",
        "lat": 11.0016, "lon": 76.9744,
        "bedsAvailable": 62, "bedsTotal": 240,
        "icuAvailable": 10, "icuStatus": "Available",
        "doctorsOnDuty": 24, "ambulancesReady": 8,
        "phone": "+91 422 230 1393",
        "emergencyContact": "CMCH Disaster Duty Officer",
        "bloodStock": {"A+": 50, "O+": 68, "B+": 42, "O-": 12, "AB+": 18}
    },
    {
        "id": "hosp-tn-tiruppur", "district": "tiruppur",
        "name": "Government Medical College Hospital, Tiruppur",
        "address": "Dharapuram Road, Tiruppur",
        "lat": 11.1020, "lon": 77.3520,
        "bedsAvailable": 35, "bedsTotal": 170,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 421 224 4566",
        "emergencyContact": "Casualty Desk",
        "bloodStock": {"A+": 25, "O+": 36, "B+": 21, "O-": 5, "AB+": 9}
    },
    {
        "id": "hosp-tn-erode", "district": "erode",
        "name": "Government Erode Medical College Hospital",
        "address": "Perundurai Highway, Erode",
        "lat": 11.2780, "lon": 77.5890,
        "bedsAvailable": 40, "bedsTotal": 190,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 15, "ambulancesReady": 6,
        "phone": "+91 4294 220 500",
        "emergencyContact": "Trauma Chief",
        "bloodStock": {"A+": 28, "O+": 40, "B+": 24, "O-": 6, "AB+": 10}
    },
    {
        "id": "hosp-tn-salem", "district": "salem",
        "name": "Govt Mohan Kumaramangalam Medical College Hospital",
        "address": "Fort Main Road, Salem",
        "lat": 11.6610, "lon": 78.1420,
        "bedsAvailable": 44, "bedsTotal": 200,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 17, "ambulancesReady": 6,
        "phone": "+91 427 221 1611",
        "emergencyContact": "Emergency Duty Desk",
        "bloodStock": {"A+": 32, "O+": 46, "B+": 27, "O-": 7, "AB+": 12}
    },
    {
        "id": "hosp-tn-namakkal", "district": "namakkal",
        "name": "Government Medical College Hospital, Namakkal",
        "address": "Siluvampatti, Namakkal",
        "lat": 11.2250, "lon": 78.1620,
        "bedsAvailable": 28, "bedsTotal": 145,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 4286 222 344",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 18, "O+": 28, "B+": 16, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-tn-dharmapuri", "district": "dharmapuri",
        "name": "Government Dharmapuri Medical College Hospital",
        "address": "Nethaji Bypass Road, Dharmapuri",
        "lat": 12.1290, "lon": 78.1640,
        "bedsAvailable": 32, "bedsTotal": 160,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 4,
        "phone": "+91 4342 233 088",
        "emergencyContact": "Trauma Unit",
        "bloodStock": {"A+": 20, "O+": 30, "B+": 18, "O-": 4, "AB+": 8}
    },
    {
        "id": "hosp-tn-krishnagiri", "district": "krishnagiri",
        "name": "Government Medical College Hospital, Krishnagiri",
        "address": "Polupalli, Krishnagiri (Near Hosur Corridor)",
        "lat": 12.5420, "lon": 78.2250,
        "bedsAvailable": 36, "bedsTotal": 175,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 5,
        "phone": "+91 4343 234 500",
        "emergencyContact": "Disaster Triage Room",
        "bloodStock": {"A+": 22, "O+": 35, "B+": 20, "O-": 5, "AB+": 9}
    },
    {
        "id": "hosp-tn-nilgiris", "district": "nilgiris",
        "name": "Government District Headquarters Hospital, Ooty",
        "address": "Hospital Road, Udhagamandalam (Ooty)",
        "lat": 11.4080, "lon": 76.7020,
        "bedsAvailable": 26, "bedsTotal": 130,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 4,
        "phone": "+91 423 244 2212",
        "emergencyContact": "Ghat Emergency Ambulance 108 Base",
        "bloodStock": {"A+": 16, "O+": 24, "B+": 14, "O-": 4, "AB+": 6}
    },

    # Central & Cauvery Delta Region
    {
        "id": "hosp-tn-trichy", "district": "trichy",
        "name": "Mahatma Gandhi Memorial Govt Hospital (MGMGH)",
        "address": "Puthur High Road, Tiruchirappalli",
        "lat": 10.8120, "lon": 78.6835,
        "bedsAvailable": 48, "bedsTotal": 210,
        "icuAvailable": 8, "icuStatus": "Available",
        "doctorsOnDuty": 18, "ambulancesReady": 7,
        "phone": "+91 431 277 0211",
        "emergencyContact": "Central Casualty Control",
        "bloodStock": {"A+": 35, "O+": 52, "B+": 30, "O-": 8, "AB+": 14}
    },
    {
        "id": "hosp-tn-thanjavur", "district": "thanjavur",
        "name": "Thanjavur Medical College Hospital (TMCH)",
        "address": "Medical College Road, Thanjavur",
        "lat": 10.7580, "lon": 79.1080,
        "bedsAvailable": 50, "bedsTotal": 220,
        "icuAvailable": 8, "icuStatus": "Available",
        "doctorsOnDuty": 20, "ambulancesReady": 7,
        "phone": "+91 4362 240 024",
        "emergencyContact": "Cauvery Delta Trauma Unit",
        "bloodStock": {"A+": 38, "O+": 55, "B+": 34, "O-": 9, "AB+": 15}
    },
    {
        "id": "hosp-tn-nagapattinam", "district": "nagapattinam",
        "name": "Government District Hospital, Nagapattinam",
        "address": "Public Office Road, Nagapattinam",
        "lat": 10.7620, "lon": 79.8400,
        "bedsAvailable": 30, "bedsTotal": 150,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 5,
        "phone": "+91 4365 222 233",
        "emergencyContact": "Coastal Emergency MO",
        "bloodStock": {"A+": 20, "O+": 30, "B+": 18, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-tn-mayiladuthurai", "district": "mayiladuthurai",
        "name": "Government District Headquarters Hospital, Mayiladuthurai",
        "address": "Kamarajar Salai, Mayiladuthurai",
        "lat": 11.1020, "lon": 79.6540,
        "bedsAvailable": 28, "bedsTotal": 140,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4364 222 240",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 18, "O+": 26, "B+": 15, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-tn-tiruvarur", "district": "tiruvarur",
        "name": "Government Tiruvarur Medical College Hospital",
        "address": "Kangany, Tiruvarur",
        "lat": 10.7810, "lon": 79.6420,
        "bedsAvailable": 35, "bedsTotal": 165,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 4,
        "phone": "+91 4366 220 020",
        "emergencyContact": "Delta Disaster Desk",
        "bloodStock": {"A+": 22, "O+": 32, "B+": 19, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-tn-karur", "district": "karur",
        "name": "Government Karur Medical College Hospital",
        "address": "Sanapiratti, Karur",
        "lat": 10.9650, "lon": 78.0820,
        "bedsAvailable": 32, "bedsTotal": 155,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 4,
        "phone": "+91 4324 255 120",
        "emergencyContact": "Casualty Officer",
        "bloodStock": {"A+": 20, "O+": 30, "B+": 17, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-tn-perambalur", "district": "perambalur",
        "name": "Government District Hospital, Perambalur",
        "address": "Trichy Main Road, Perambalur",
        "lat": 11.2310, "lon": 78.8780,
        "bedsAvailable": 24, "bedsTotal": 130,
        "icuAvailable": 3, "icuStatus": "Available",
        "doctorsOnDuty": 9, "ambulancesReady": 3,
        "phone": "+91 4328 277 220",
        "emergencyContact": "Emergency Desk",
        "bloodStock": {"A+": 14, "O+": 22, "B+": 13, "O-": 3, "AB+": 5}
    },
    {
        "id": "hosp-tn-ariyalur", "district": "ariyalur",
        "name": "Government Ariyalur Medical College Hospital",
        "address": "Collectorate Road, Ariyalur",
        "lat": 11.1440, "lon": 79.0720,
        "bedsAvailable": 28, "bedsTotal": 140,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 10, "ambulancesReady": 3,
        "phone": "+91 4329 222 300",
        "emergencyContact": "Casualty Desk",
        "bloodStock": {"A+": 16, "O+": 25, "B+": 15, "O-": 4, "AB+": 6}
    },
    {
        "id": "hosp-tn-pudukkottai", "district": "pudukkottai",
        "name": "Government Pudukkottai Medical College Hospital",
        "address": "Pillathanvayal, Pudukkottai",
        "lat": 10.3720, "lon": 78.8150,
        "bedsAvailable": 34, "bedsTotal": 160,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 4,
        "phone": "+91 4322 222 450",
        "emergencyContact": "Trauma Triage",
        "bloodStock": {"A+": 22, "O+": 32, "B+": 18, "O-": 5, "AB+": 8}
    },

    # Southern Region
    {
        "id": "hosp-tn-madurai", "district": "madurai",
        "name": "Government Rajaji Hospital (GRH Madurai)",
        "address": "Alagar Kovil Road, Goripalayam, Madurai",
        "lat": 9.9325, "lon": 78.1345,
        "bedsAvailable": 65, "bedsTotal": 260,
        "icuAvailable": 12, "icuStatus": "Available",
        "doctorsOnDuty": 26, "ambulancesReady": 9,
        "phone": "+91 452 253 2535",
        "emergencyContact": "GRH South TN Trauma Wing",
        "bloodStock": {"A+": 55, "O+": 74, "B+": 46, "O-": 14, "AB+": 22}
    },
    {
        "id": "hosp-tn-dindigul", "district": "dindigul",
        "name": "Government Dindigul Medical College Hospital",
        "address": "Trichy Road, Dindigul",
        "lat": 10.3720, "lon": 77.9890,
        "bedsAvailable": 34, "bedsTotal": 165,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 4,
        "phone": "+91 451 242 3444",
        "emergencyContact": "Casualty Duty Desk",
        "bloodStock": {"A+": 22, "O+": 33, "B+": 19, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-tn-theni", "district": "theni",
        "name": "Government Theni Medical College Hospital",
        "address": "Kanoor Vilakku, Aundipatti, Theni",
        "lat": 9.9880, "lon": 77.5320,
        "bedsAvailable": 36, "bedsTotal": 170,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 14, "ambulancesReady": 5,
        "phone": "+91 4546 244 500",
        "emergencyContact": "Ghat Ambulance Base",
        "bloodStock": {"A+": 24, "O+": 35, "B+": 20, "O-": 5, "AB+": 9}
    },
    {
        "id": "hosp-tn-virudhunagar", "district": "virudhunagar",
        "name": "Government Medical College Hospital, Virudhunagar",
        "address": "Collectorate Road, Virudhunagar",
        "lat": 9.5780, "lon": 77.9620,
        "bedsAvailable": 32, "bedsTotal": 155,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 12, "ambulancesReady": 4,
        "phone": "+91 4562 252 300",
        "emergencyContact": "Industrial Fire & Trauma Unit",
        "bloodStock": {"A+": 20, "O+": 30, "B+": 18, "O-": 4, "AB+": 8}
    },
    {
        "id": "hosp-tn-sivaganga", "district": "sivaganga",
        "name": "Government Sivaganga Medical College Hospital",
        "address": "Madurai Road, Sivaganga",
        "lat": 9.8510, "lon": 78.4720,
        "bedsAvailable": 30, "bedsTotal": 150,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4575 240 400",
        "emergencyContact": "Casualty Room",
        "bloodStock": {"A+": 19, "O+": 28, "B+": 16, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-tn-ramanathapuram", "district": "ramanathapuram",
        "name": "Government Ramanathapuram Medical College Hospital",
        "address": "Kenikarai, Ramanathapuram",
        "lat": 9.3710, "lon": 78.8450,
        "bedsAvailable": 35, "bedsTotal": 165,
        "icuAvailable": 5, "icuStatus": "Available",
        "doctorsOnDuty": 13, "ambulancesReady": 5,
        "phone": "+91 4567 220 250",
        "emergencyContact": "Island & Coastal Trauma Desk",
        "bloodStock": {"A+": 22, "O+": 34, "B+": 19, "O-": 5, "AB+": 8}
    },
    {
        "id": "hosp-tn-thoothukudi", "district": "thoothukudi",
        "name": "Government Thoothukudi Medical College Hospital (TKMCH)",
        "address": "Kamraj Nagar, 3rd Mile, Thoothukudi",
        "lat": 8.7820, "lon": 80.1240,
        "bedsAvailable": 45, "bedsTotal": 190,
        "icuAvailable": 7, "icuStatus": "Available",
        "doctorsOnDuty": 17, "ambulancesReady": 6,
        "phone": "+91 461 238 2000",
        "emergencyContact": "Port Disaster Casualty Unit",
        "bloodStock": {"A+": 30, "O+": 44, "B+": 26, "O-": 7, "AB+": 11}
    },
    {
        "id": "hosp-tn-tirunelveli", "district": "tirunelveli",
        "name": "Tirunelveli Medical College Hospital (TvMCH)",
        "address": "High Ground, Palayamkottai, Tirunelveli",
        "lat": 8.7230, "lon": 77.7420,
        "bedsAvailable": 52, "bedsTotal": 210,
        "icuAvailable": 8, "icuStatus": "Available",
        "doctorsOnDuty": 20, "ambulancesReady": 7,
        "phone": "+91 462 257 2733",
        "emergencyContact": "Thamirabarani Flood Trauma Unit",
        "bloodStock": {"A+": 36, "O+": 52, "B+": 31, "O-": 8, "AB+": 14}
    },
    {
        "id": "hosp-tn-tenkasi", "district": "tenkasi",
        "name": "Government District Headquarters Hospital, Tenkasi",
        "address": "Madan Kovil Street, Tenkasi",
        "lat": 8.9610, "lon": 77.3180,
        "bedsAvailable": 28, "bedsTotal": 140,
        "icuAvailable": 4, "icuStatus": "Available",
        "doctorsOnDuty": 11, "ambulancesReady": 4,
        "phone": "+91 4633 222 240",
        "emergencyContact": "Courtallam Flash Flood Duty MO",
        "bloodStock": {"A+": 18, "O+": 27, "B+": 15, "O-": 4, "AB+": 7}
    },
    {
        "id": "hosp-tn-kanyakumari", "district": "kanyakumari",
        "name": "Kanyakumari Govt Medical College Hospital (Asaripallam)",
        "address": "Asaripallam, Nagercoil, Kanniyakumari",
        "lat": 8.1920, "lon": 77.4080,
        "bedsAvailable": 42, "bedsTotal": 180,
        "icuAvailable": 6, "icuStatus": "Available",
        "doctorsOnDuty": 16, "ambulancesReady": 5,
        "phone": "+91 4652 223 201",
        "emergencyContact": "Coastal Rescue Medical Officer",
        "bloodStock": {"A+": 28, "O+": 40, "B+": 23, "O-": 6, "AB+": 10}
    }
]

SHELTERS_TN_ALL = [
    {
        "id": "sh-tn-cuddalore", "district": "cuddalore",
        "name": "Multipurpose Cyclone Shelter (MPCS) - Devanampattinam",
        "address": "Devanampattinam Seashore, Cuddalore Port",
        "lat": 11.7510, "lon": 79.7820,
        "capacity": 900, "occupied": 560,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-chennai-1", "district": "chennai",
        "name": "GCC Central Flood Evacuation Shelter (Ripon Building Zone)",
        "address": "Sydenhams Road, Periamet, Chennai",
        "lat": 13.0825, "lon": 80.2740,
        "capacity": 700, "occupied": 440,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-chennai-2", "district": "chennai",
        "name": "GCC Relief Camp - Velachery Community Hall",
        "address": "Gandhi Salai, Velachery, Chennai",
        "lat": 12.9810, "lon": 80.2180,
        "capacity": 500, "occupied": 420,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": False, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-nagapattinam", "district": "nagapattinam",
        "name": "Velankanni Multipurpose Cyclone Shelter",
        "address": "Main Coast Road, Velankanni, Nagapattinam",
        "lat": 10.6830, "lon": 79.8490,
        "capacity": 1200, "occupied": 680,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-madurai", "district": "madurai",
        "name": "Madurai Corporation Disaster Relief Center (Tamukkam)",
        "address": "Tamukkam Ground Complex, Tallakulam, Madurai",
        "lat": 9.9350, "lon": 78.1380,
        "capacity": 600, "occupied": 210,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": False, "wheelchair": True
    },
    {
        "id": "sh-tn-coimbatore", "district": "coimbatore",
        "name": "Coimbatore Corporation Relief Center (RS Puram)",
        "address": "DB Road, RS Puram, Coimbatore",
        "lat": 11.0110, "lon": 76.9450,
        "capacity": 500, "occupied": 160,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-trichy", "district": "trichy",
        "name": "Srirangam Cauvery Flood Relief Camp",
        "address": "North Devi Street, Srirangam, Tiruchirappalli",
        "lat": 10.8620, "lon": 78.6920,
        "capacity": 450, "occupied": 220,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": False, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-kanyakumari", "district": "kanyakumari",
        "name": "Colachel Coastal Cyclone Evacuation Center",
        "address": "Harbour Road, Colachel, Kanniyakumari",
        "lat": 8.1780, "lon": 77.2580,
        "capacity": 750, "occupied": 310,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-ramanathapuram", "district": "ramanathapuram",
        "name": "Rameswaram Island Coastal Cyclone Shelter",
        "address": "Dhanushkodi Bypass Road, Rameswaram",
        "lat": 9.2880, "lon": 79.3120,
        "capacity": 850, "occupied": 390,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-mayiladuthurai", "district": "mayiladuthurai",
        "name": "Poompuhar Coastal Disaster Relief Center",
        "address": "Kaveripoompattinam Shore, Mayiladuthurai",
        "lat": 11.1480, "lon": 79.8540,
        "capacity": 600, "occupied": 240,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-viluppuram", "district": "viluppuram",
        "name": "Marakkanam Coastal Cyclone Evacuation Center",
        "address": "East Coast Road (ECR), Marakkanam, Viluppuram",
        "lat": 12.1980, "lon": 79.9480,
        "capacity": 650, "occupied": 260,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-tirunelveli", "district": "tirunelveli",
        "name": "Thamirabarani Basin Flood Relief Camp (Kokkirakulam)",
        "address": "Kokkirakulam River Road, Tirunelveli",
        "lat": 8.7310, "lon": 77.7280,
        "capacity": 480, "occupied": 190,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": False, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-nilgiris", "district": "nilgiris",
        "name": "Nilgiris Landslide Emergency Evacuation Center",
        "address": "ATC Bus Stand Ground, Ooty (Nilgiris)",
        "lat": 11.4120, "lon": 76.6980,
        "capacity": 400, "occupied": 140,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": True, "wheelchair": False
    },
    {
        "id": "sh-tn-thanjavur", "district": "thanjavur",
        "name": "Thanjavur Vennar Basin Flood Evacuation Center",
        "address": "Karanthai, Thanjavur",
        "lat": 10.7960, "lon": 79.1410,
        "capacity": 550, "occupied": 210,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": True, "wheelchair": True
    },
    {
        "id": "sh-tn-salem", "district": "salem",
        "name": "Salem Corporation Disaster Relief Shelter",
        "address": "Fort Ground, Salem",
        "lat": 11.6580, "lon": 78.1520,
        "capacity": 450, "occupied": 120,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": True, "womenOnly": False, "wheelchair": True
    },
    {
        "id": "sh-tn-erode", "district": "erode",
        "name": "Bhavani Kooduthurai Flood Relief Shelter",
        "address": "River Confluence Road, Bhavani, Erode",
        "lat": 11.4480, "lon": 77.6820,
        "capacity": 420, "occupied": 180,
        "foodAvailable": True, "medicalSupport": True, "petFriendly": False, "womenOnly": True, "wheelchair": True
    }
]

FOOD_CENTERS_TN = [
    {
        "id": "fd-tn-chennai", "district": "chennai",
        "name": "Tamil Nadu Civil Supplies Corporation (TNCSC) Central Depot",
        "address": "Greams Road, Thousand Lights, Chennai",
        "lat": 13.0580, "lon": 80.2520,
        "riceKg": 25000, "waterLiters": 60000, "blankets": 4500, "medicineKits": 2000,
        "operator": "TNCSC & Greater Chennai Corporation"
    },
    {
        "id": "fd-tn-thanjavur", "district": "thanjavur",
        "name": "TNCSC Delta Granary & Emergency Supply Depot",
        "address": "Railway Station Road, Thanjavur",
        "lat": 10.7810, "lon": 79.1320,
        "riceKg": 42000, "waterLiters": 35000, "blankets": 3100, "medicineKits": 1200,
        "operator": "TNCSC Delta Zonal Command"
    },
    {
        "id": "fd-tn-coimbatore", "district": "coimbatore",
        "name": "Coimbatore District Relief Distribution Warehouse",
        "address": "Cross Cut Road, Gandhipuram, Coimbatore",
        "lat": 11.0190, "lon": 76.9680,
        "riceKg": 18000, "waterLiters": 38000, "blankets": 2400, "medicineKits": 1100,
        "operator": "Indian Red Cross Society Coimbatore"
    },
    {
        "id": "fd-tn-madurai", "district": "madurai",
        "name": "Madurai District Relief Depot (Anna Nagar Hub)",
        "address": "Kuruvikaran Salai, Anna Nagar, Madurai",
        "lat": 9.9180, "lon": 78.1480,
        "riceKg": 15000, "waterLiters": 32000, "blankets": 2200, "medicineKits": 950,
        "operator": "Madurai District Administration"
    },
    {
        "id": "fd-tn-cuddalore", "district": "cuddalore",
        "name": "Cuddalore Coastal Cyclone Relief Hub",
        "address": "Beach Road, Cuddalore Port",
        "lat": 11.7420, "lon": 79.7760,
        "riceKg": 16000, "waterLiters": 45000, "blankets": 3500, "medicineKits": 1600,
        "operator": "National Disaster Relief & TNSDMA"
    },
    {
        "id": "fd-tn-tirunelveli", "district": "tirunelveli",
        "name": "Tirunelveli District Disaster Supply Depot",
        "address": "Tiruchendur Road, Palayamkottai, Tirunelveli",
        "lat": 8.7180, "lon": 77.7480,
        "riceKg": 12000, "waterLiters": 28000, "blankets": 1900, "medicineKits": 800,
        "operator": "Tirunelveli Collectorate Supply Unit"
    },
    {
        "id": "fd-tn-salem", "district": "salem",
        "name": "Salem Zonal Civil Supplies Distribution Depot",
        "address": "Collectorate Road, Salem",
        "lat": 11.6620, "lon": 78.1490,
        "riceKg": 14000, "waterLiters": 26000, "blankets": 1700, "medicineKits": 750,
        "operator": "TNCSC Salem Zone"
    },
    {
        "id": "fd-tn-vellore", "district": "vellore",
        "name": "Vellore District Essential Supplies Depot",
        "address": "Katpadi Road, Vellore",
        "lat": 12.9320, "lon": 79.1390,
        "riceKg": 13000, "waterLiters": 24000, "blankets": 1600, "medicineKits": 700,
        "operator": "Vellore Red Cross & Civil Supplies"
    }
]

BLOOD_BANKS_TN = [
    {
        "id": "bb-tn-chennai", "district": "chennai",
        "name": "TANSACS Central Blood Bank (RGGGH), Chennai",
        "address": "EVR Periyar Salai, Park Town, Chennai",
        "lat": 13.0805, "lon": 80.2778,
        "phone": "+91 44 2530 5140",
        "inventory": {"O+": 95, "O-": 22, "A+": 78, "A-": 18, "B+": 64, "B-": 14, "AB+": 32, "AB-": 8}
    },
    {
        "id": "bb-tn-coimbatore", "district": "coimbatore",
        "name": "Coimbatore CMCH Blood Bank & Transfusion Center",
        "address": "Trichy Road, Coimbatore",
        "lat": 11.0016, "lon": 76.9744,
        "phone": "+91 422 230 1393",
        "inventory": {"O+": 68, "O-": 12, "A+": 48, "A-": 9, "B+": 40, "B-": 8, "AB+": 20, "AB-": 5}
    },
    {
        "id": "bb-tn-madurai", "district": "madurai",
        "name": "Government Rajaji Hospital Blood Bank, Madurai",
        "address": "Goripalayam, Madurai",
        "lat": 9.9325, "lon": 78.1345,
        "phone": "+91 452 253 2535",
        "inventory": {"O+": 60, "O-": 10, "A+": 42, "A-": 8, "B+": 36, "B-": 7, "AB+": 16, "AB-": 4}
    },
    {
        "id": "bb-tn-trichy", "district": "trichy",
        "name": "MGMGH Blood Bank, Puthur, Tiruchirappalli",
        "address": "Puthur High Road, Trichy",
        "lat": 10.8120, "lon": 78.6835,
        "phone": "+91 431 277 0211",
        "inventory": {"O+": 48, "O-": 8, "A+": 34, "A-": 6, "B+": 29, "B-": 5, "AB+": 14, "AB-": 3}
    },
    {
        "id": "bb-tn-salem", "district": "salem",
        "name": "Salem Mohan Kumaramangalam GMKMC Blood Bank",
        "address": "Fort Main Road, Salem",
        "lat": 11.6610, "lon": 78.1420,
        "phone": "+91 427 221 1611",
        "inventory": {"O+": 40, "O-": 7, "A+": 28, "A-": 5, "B+": 24, "B-": 4, "AB+": 11, "AB-": 3}
    },
    {
        "id": "bb-tn-tirunelveli", "district": "tirunelveli",
        "name": "Tirunelveli Medical College Hospital Blood Bank",
        "address": "Palayamkottai, Tirunelveli",
        "lat": 8.7230, "lon": 77.7420,
        "phone": "+91 462 257 2733",
        "inventory": {"O+": 44, "O-": 8, "A+": 30, "A-": 6, "B+": 26, "B-": 5, "AB+": 12, "AB-": 3}
    },
    {
        "id": "bb-tn-vellore", "district": "vellore",
        "name": "CMC Hospital Blood Transfusion Center, Vellore",
        "address": "Ida Scudder Road, Vellore",
        "lat": 12.9250, "lon": 79.1350,
        "phone": "+91 416 228 2000",
        "inventory": {"O+": 85, "O-": 18, "A+": 65, "A-": 14, "B+": 55, "B-": 12, "AB+": 28, "AB-": 7}
    }
]

EMERGENCIES_TN = [
    {
        "id": "em-tn-1", "district": "chennai", "type": "flood",
        "title": "Velachery & Pallikaranai Inundation (Depth: 1.6m)",
        "description": "Adyar overflow inundated residential streets. 18 families stranded on 2nd floor terraces. Boat evacuation requested.",
        "lat": 12.9750, "lon": 80.2190,
        "status": "Active", "priority": "Critical",
        "createdAt": "2026-10-19T08:30:00Z",
        "photo": "https://images.unsplash.com/photo-1547683905-f686c993aae5?w=300"
    },
    {
        "id": "em-tn-2", "district": "cuddalore", "type": "flood",
        "title": "Pennaiyar River Surge & Coastal Storm Inundation",
        "description": "Low-lying fishing hamlets near Cuddalore Old Town flooded. Multipurpose shelters activated.",
        "lat": 11.7450, "lon": 79.7680,
        "status": "Assigned", "priority": "Critical", "volunteer": "NDRF 4th Battalion",
        "createdAt": "2026-10-19T07:45:00Z",
        "photo": "https://images.unsplash.com/photo-1514632595-4944383f2737?w=300"
    },
    {
        "id": "em-tn-3", "district": "chennai", "type": "fire",
        "title": "Manali Industrial Petrochemical Storage Fire",
        "description": "Refinery complex tank fire with chemical smoke drifting towards Thiruvottiyur. Fire & Rescue Services on scene.",
        "lat": 13.1670, "lon": 80.2640,
        "status": "Active", "priority": "Critical",
        "createdAt": "2026-10-19T08:15:00Z",
        "photo": "https://images.unsplash.com/photo-1542385151-efd9000785a0?w=300"
    },
    {
        "id": "em-tn-4", "district": "coimbatore", "type": "fire",
        "title": "SIDCO Kurichi Industrial Cotton Warehouse Blaze",
        "description": "Major fire in textile storage depot. 6 fire tenders deployed from Coimbatore Central Station.",
        "lat": 10.9420, "lon": 76.9710,
        "status": "Active", "priority": "High",
        "createdAt": "2026-10-19T07:20:00Z",
        "photo": None
    },
    {
        "id": "em-tn-5", "district": "trichy", "type": "flood",
        "title": "Cauvery River High Water Alert - Srirangam Lowland",
        "description": "Heavy discharge from Mettur dam resulted in riverbanks spilling near Amma Mandapam ghats.",
        "lat": 10.8580, "lon": 78.6880,
        "status": "Reported", "priority": "Medium",
        "createdAt": "2026-10-19T06:50:00Z",
        "photo": None
    },
    {
        "id": "em-tn-6", "district": "nilgiris", "type": "blocked",
        "title": "Mettupalayam - Coonoor Ghat Road Landslide (NH 181)",
        "description": "Massive boulder fall and uprooted trees near Marappalam. Traffic halted both directions. Highway department clearing.",
        "lat": 11.3520, "lon": 76.8120,
        "status": "Reported", "priority": "High",
        "createdAt": "2026-10-19T06:30:00Z",
        "photo": None
    },
    {
        "id": "em-tn-7", "district": "tirunelveli", "type": "flood",
        "title": "Thamirabarani River Breach near Vannarpettai",
        "description": "Water reached 1 meter on riverside service lanes. Traffic diverted through Palayamkottai High Ground.",
        "lat": 8.7280, "lon": 77.7320,
        "status": "Reported", "priority": "High",
        "createdAt": "2026-10-19T06:10:00Z",
        "photo": None
    },
    {
        "id": "em-tn-8", "district": "chennai", "type": "blocked",
        "title": "East Coast Road (ECR) Inundation near Akkarai",
        "description": "High storm surge washed over highway. Road closed for heavy vehicles. Detour via OMR.",
        "lat": 12.8920, "lon": 80.2450,
        "status": "Reported", "priority": "Medium",
        "createdAt": "2026-10-19T05:50:00Z",
        "photo": None
    }
]

VOLUNTEERS_TN = [
    {"id": "v-tn-1", "name": "TNDRF Squad Alpha (Chennai)", "skills": "Deep Water Rescue / Inflatable Boats", "status": "En Route", "tasks": 2, "lat": 13.078, "lon": 80.255},
    {"id": "v-tn-2", "name": "Karthik Subramanian", "skills": "Paramedic / Trauma First Aid", "status": "Assigned", "tasks": 1, "lat": 12.981, "lon": 80.220},
    {"id": "v-tn-3", "name": "NDRF 4th Battalion (Arakkonam & Cuddalore Wing)", "skills": "Coastal Flood Rescue / Tree Cutting", "status": "Assigned", "tasks": 1, "lat": 11.748, "lon": 79.771},
    {"id": "v-tn-4", "name": "Ananya Ramesh", "skills": "Triage / Tamil-English Translation / Logistics", "status": "Available", "tasks": 0, "lat": 11.012, "lon": 76.950},
    {"id": "v-tn-5", "name": "Madurai Disaster Youth Volunteer Wing", "skills": "Food Distribution & Evacuation", "status": "Available", "tasks": 0, "lat": 9.930, "lon": 78.125},
    {"id": "v-tn-6", "name": "Nilgiris Mountain Rescue Club", "skills": "Ghat Landslide Clearing / High Altitude First Aid", "status": "Available", "tasks": 0, "lat": 11.410, "lon": 76.695},
    {"id": "v-tn-7", "name": "Trichy Delta Flood Relief Corps", "skills": "River Patrol / Sandbag Embankment", "status": "Available", "tasks": 0, "lat": 10.795, "lon": 78.700}
]

MISSING_PERSONS_TN = [
    {
        "id": "mp-tn-1", "district": "cuddalore",
        "name": "Murugan Velu", "age": 48,
        "lastSeen": "Devanampattinam shore while securing country craft catamaran",
        "description": "Wearing green checked lungi, blue shirt. Fishermen community badge on wrist.",
        "contact": "+91 94432 10982", "status": "Missing",
        "photo": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200"
    },
    {
        "id": "mp-tn-2", "district": "chennai",
        "name": "Lakshmi Ammal", "age": 74,
        "lastSeen": "Separated near Velachery AGS colony during rescue boat transfer",
        "description": "Wearing maroon saree, spectacles, hearing aid in right ear. Speaks Tamil.",
        "contact": "+91 98401 55219", "status": "Missing",
        "photo": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200"
    },
    {
        "id": "mp-tn-3", "district": "nagapattinam",
        "name": "Kavin Selvan", "age": 11,
        "lastSeen": "Velankanni church relief shelter queue",
        "description": "Wearing blue school uniform shorts, yellow raincoat. Has asthma inhaler in pouch.",
        "contact": "+91 94444 88123", "status": "Found",
        "photo": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=200"
    }
]

print("Datasets ready: 38 hospitals, 16 shelters, 8 food centers, 7 blood banks, 8 emergencies.")

import os

with open("static/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update district selector options
old_select_pattern = r'<select id="districtSelector" class="district-select-box"[^>]*>.*?</select>'

new_select_html = '''<select id="districtSelector" class="district-select-box" aria-label="Select Tamil Nadu District">
              <option value="all">📍 All Tamil Nadu (Statewide Overview)</option>
              <optgroup label="── Chennai Metropolitan Area ──">
                <option value="chennai" selected>🏙️ Chennai (State Capital)</option>
                <option value="chengalpattu">🏙️ Chengalpattu</option>
                <option value="kancheepuram">🏛️ Kancheepuram (Silk & Temples)</option>
                <option value="tiruvallur">🏭 Tiruvallur (Industrial Hub)</option>
              </optgroup>
              <optgroup label="── Northern Region ──">
                <option value="cuddalore">🌊 Cuddalore (Coastal Surge Zone)</option>
                <option value="viluppuram">🌾 Viluppuram</option>
                <option value="kallakurichi">🌾 Kallakurichi</option>
                <option value="vellore">🏙️ Vellore (CMC & Fort)</option>
                <option value="ranipet">🏭 Ranipet</option>
                <option value="tirupathur">🌄 Tirupathur</option>
                <option value="tiruvannamalai">⛰️ Tiruvannamalai (Annamalai)</option>
              </optgroup>
              <optgroup label="── Western (Kongu) Region ──">
                <option value="coimbatore">🏙️ Coimbatore (Kongu Capital)</option>
                <option value="tiruppur">👕 Tiruppur (Knitwear Hub)</option>
                <option value="erode">🏭 Erode (Turmeric & River Basin)</option>
                <option value="salem">⛰️ Salem (Steel & Mango City)</option>
                <option value="namakkal">🥚 Namakkal (Poultry & Transport)</option>
                <option value="dharmapuri">🥭 Dharmapuri</option>
                <option value="krishnagiri">🏭 Krishnagiri / Hosur Tech Corridor</option>
                <option value="nilgiris">🏔️ Nilgiris / Ooty (Western Ghats)</option>
              </optgroup>
              <optgroup label="── Central & Cauvery Delta Region ──">
                <option value="trichy">🏙️ Tiruchirappalli (Trichy Central)</option>
                <option value="thanjavur">🌾 Thanjavur (Cauvery Delta Granary)</option>
                <option value="nagapattinam">🌊 Nagapattinam (Delta Coast)</option>
                <option value="mayiladuthurai">🌊 Mayiladuthurai</option>
                <option value="tiruvarur">🌾 Tiruvarur</option>
                <option value="karur">🏭 Karur (Textile & Amaravathi)</option>
                <option value="perambalur">🌾 Perambalur</option>
                <option value="ariyalur">🏭 Ariyalur (Cement Hub)</option>
                <option value="pudukkottai">🏛️ Pudukkottai</option>
              </optgroup>
              <optgroup label="── Southern Region ──">
                <option value="madurai">🏙️ Madurai (Cultural Capital)</option>
                <option value="dindigul">⛰️ Dindigul (Lock City)</option>
                <option value="theni">🌄 Theni (Cardamom Hills)</option>
                <option value="virudhunagar">🏭 Virudhunagar / Sivakasi</option>
                <option value="sivaganga">🏛️ Sivaganga / Karaikudi</option>
                <option value="ramanathapuram">🌊 Ramanathapuram / Rameswaram</option>
                <option value="thoothukudi">⚓ Thoothukudi (VOC Port City)</option>
                <option value="tirunelveli">🏙️ Tirunelveli (Halwa & River City)</option>
                <option value="tenkasi">🌊 Tenkasi / Courtallam Falls</option>
                <option value="kanyakumari">🌊 Kanniyakumari (Cape Comorin)</option>
              </optgroup>
            </select>'''

content = re.sub(old_select_pattern, new_select_html, content, flags=re.DOTALL)

# 2. Add Search button right next to mapSearchInput
search_row_pattern = r'<input type="text" id="mapSearchInput"[^>]*>'
search_btn_html = '''<input type="text" id="mapSearchInput" class="search-input-box" placeholder="Search any place in Tamil Nadu (e.g. Kumbakonam, Hosur, RGGGH, Velankanni, Ooty)...">
            <button class="btn-action-primary" id="btnGeocodeSearch" title="Search any town, taluk, village or landmark in Tamil Nadu">🔍 Search</button>'''

content = re.sub(search_row_pattern, search_btn_html, content)

# 3. Add District filter on Hospitals Tab
hosp_header_pattern = r'<div class="tag-chips">\s*<span class="badge badge-success">Tamil Nadu Health Systems Active</span>\s*</div>'
hosp_filter_html = '''<div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
              <select id="hospitalDistrictFilter" class="district-select-box" style="font-size:12px; padding:6px 10px;">
                <option value="all">📍 All Tamil Nadu (38 Districts)</option>
                <option value="chennai">Chennai</option>
                <option value="chengalpattu">Chengalpattu</option>
                <option value="kancheepuram">Kancheepuram</option>
                <option value="tiruvallur">Tiruvallur</option>
                <option value="cuddalore">Cuddalore</option>
                <option value="viluppuram">Viluppuram</option>
                <option value="kallakurichi">Kallakurichi</option>
                <option value="vellore">Vellore</option>
                <option value="ranipet">Ranipet</option>
                <option value="tirupathur">Tirupathur</option>
                <option value="tiruvannamalai">Tiruvannamalai</option>
                <option value="coimbatore">Coimbatore</option>
                <option value="tiruppur">Tiruppur</option>
                <option value="erode">Erode</option>
                <option value="salem">Salem</option>
                <option value="namakkal">Namakkal</option>
                <option value="dharmapuri">Dharmapuri</option>
                <option value="krishnagiri">Krishnagiri / Hosur</option>
                <option value="nilgiris">Nilgiris / Ooty</option>
                <option value="trichy">Tiruchirappalli (Trichy)</option>
                <option value="thanjavur">Thanjavur</option>
                <option value="nagapattinam">Nagapattinam</option>
                <option value="mayiladuthurai">Mayiladuthurai</option>
                <option value="tiruvarur">Tiruvarur</option>
                <option value="karur">Karur</option>
                <option value="perambalur">Perambalur</option>
                <option value="ariyalur">Ariyalur</option>
                <option value="pudukkottai">Pudukkottai</option>
                <option value="madurai">Madurai</option>
                <option value="dindigul">Dindigul</option>
                <option value="theni">Theni</option>
                <option value="virudhunagar">Virudhunagar</option>
                <option value="sivaganga">Sivaganga</option>
                <option value="ramanathapuram">Ramanathapuram</option>
                <option value="thoothukudi">Thoothukudi</option>
                <option value="tirunelveli">Tirunelveli</option>
                <option value="tenkasi">Tenkasi</option>
                <option value="kanyakumari">Kanniyakumari</option>
              </select>
              <span class="badge badge-success">38 District Headquarters Active</span>
            </div>'''
content = re.sub(hosp_header_pattern, hosp_filter_html, content)

# 4. Add District filter on Shelters Tab
shelter_btn_pattern = r'<button class="btn-action-primary" id="addShelterBtn"[^>]*>⛺ Register New Shelter</button>'
shelter_filter_html = '''<div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
              <select id="shelterDistrictFilter" class="district-select-box" style="font-size:12px; padding:6px 10px;">
                <option value="all">📍 All Tamil Nadu Shelters</option>
                <option value="cuddalore">Cuddalore (MPCS)</option>
                <option value="nagapattinam">Nagapattinam (Velankanni MPCS)</option>
                <option value="chennai">Chennai (GCC Shelters)</option>
                <option value="ramanathapuram">Ramanathapuram (Rameswaram Island)</option>
                <option value="mayiladuthurai">Mayiladuthurai (Poompuhar Coast)</option>
                <option value="kanyakumari">Kanniyakumari (Colachel Shore)</option>
                <option value="viluppuram">Viluppuram (Marakkanam ECR)</option>
                <option value="madurai">Madurai (Tamukkam Ground)</option>
                <option value="coimbatore">Coimbatore (RS Puram Center)</option>
                <option value="trichy">Trichy (Srirangam Cauvery Camp)</option>
                <option value="thanjavur">Thanjavur (Vennar Basin)</option>
                <option value="tirunelveli">Tirunelveli (Thamirabarani Camp)</option>
                <option value="nilgiris">Nilgiris (Ooty Landslide Shelter)</option>
                <option value="erode">Erode (Bhavani Flood Camp)</option>
                <option value="salem">Salem (Corporation Shelter)</option>
              </select>
              <button class="btn-action-primary" id="addShelterBtn" style="display: none;">⛺ Register New Shelter</button>
            </div>'''
content = re.sub(shelter_btn_pattern, shelter_filter_html, content)

# 5. Build and inject JS data
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.generate_tn_data import TN_DISTRICTS

js_districts_str = json.dumps(TN_DISTRICTS, indent=6)
js_hospitals_str = json.dumps(HOSPITALS_TN_38, indent=8)
js_shelters_str = json.dumps(SHELTERS_TN_ALL, indent=8)
js_food_str = json.dumps(FOOD_CENTERS_TN, indent=8)
js_blood_str = json.dumps(BLOOD_BANKS_TN, indent=8)
js_emergencies_str = json.dumps(EMERGENCIES_TN, indent=8)
js_volunteers_str = json.dumps(VOLUNTEERS_TN, indent=8)
js_missing_str = json.dumps(MISSING_PERSONS_TN, indent=8)

new_js_data_block = f"""    // ================= DATA STORE WITH REALISTIC 38-DISTRICT TAMIL NADU DISASTER DATA =================
    const STORAGE_KEY = 'resqcommand_tamilnadu_38districts_v5';

    // Comprehensive 38 District Centroids & Zoom levels
    const TN_DISTRICTS = {js_districts_str};

    const TAMILNADU_INITIAL_STATE = {{
      emergencies: {js_emergencies_str},
      hospitals: {js_hospitals_str},
      shelters: {js_shelters_str},
      foodCenters: {js_food_str},
      bloodBanks: {js_blood_str},
      volunteers: {js_volunteers_str},
      missingPersons: {js_missing_str},
      broadcastAlert: {{
        severity: 'CYCLONE & FLOOD WARNING',
        message: '⚠️ TNSDMA Alert: Active disaster monitoring across all 38 districts of Tamil Nadu. High discharge alert in Cauvery & Thamirabarani basins. Coastal storm watch for Chennai, Cuddalore, Delta & Gulf of Mannar.'
      }}
    }};"""

# Replace the existing initial data block
old_data_pattern = r'// ================= DATA STORE WITH REALISTIC TAMIL NADU DISASTER DATA =================.*?const TAMILNADU_INITIAL_STATE = \{.*?broadcastAlert: \{.*?\}\s*\};'
content = re.sub(old_data_pattern, new_js_data_block, content, flags=re.DOTALL)

# 6. Add geocoding search and district filter handlers in JS
geocode_and_filter_js = """
    // ================= GEOLOCATION & TN TOWN GEOCODING SEARCH =================
    let searchHighlightMarker = null;

    async function performGeocodeSearch(rawQuery) {
      if (!rawQuery || !rawQuery.trim()) return;
      const q = rawQuery.trim();
      const qLower = q.toLowerCase();

      // Check if user entered a district name directly
      for (const [key, dist] of Object.entries(TN_DISTRICTS)) {
        if (key === qLower || dist.name.toLowerCase().includes(qLower)) {
          document.getElementById('districtSelector').value = key;
          currentDistrict = key;
          map.flyTo([dist.lat, dist.lon], dist.zoom, { duration: 1.2 });
          showNotification(`📍 Centered on ${dist.name}`, 'info');
          return;
        }
      }

      // Otherwise, call Nominatim Geocoding API via backend for any town/locality in Tamil Nadu
      const searchBtn = document.getElementById('btnGeocodeSearch');
      const originalText = searchBtn.textContent;
      searchBtn.textContent = '⏳ Searching...';
      searchBtn.disabled = true;

      try {
        const queryWithContext = q.toLowerCase().includes('tamil nadu') ? q : `${q}, Tamil Nadu`;
        const res = await fetch(`/api/geocode?q=${encodeURIComponent(queryWithContext)}`);
        if (!res.ok) throw new Error('Geocoding service unavailable');
        const data = await res.json();
        
        if (data.results && data.results.length > 0) {
          const topResult = data.results[0];
          const lat = topResult.lat;
          const lon = topResult.lon;

          map.flyTo([lat, lon], 14, { duration: 1.2 });

          if (searchHighlightMarker) map.removeLayer(searchHighlightMarker);
          searchHighlightMarker = L.marker([lat, lon], {
            icon: L.divIcon({
              className: 'custom-search-pin',
              html: '<div style="background:#3b82f6; color:#fff; border-radius:50%; width:36px; height:36px; display:flex; align-items:center; justify-content:center; font-size:18px; border:2px solid #fff; box-shadow:0 0 16px #3b82f6; animation:sosPulse 1.5s infinite;">📍</div>',
              iconSize: [36, 36],
              iconAnchor: [18, 18]
            })
          }).addTo(map);

          searchHighlightMarker.bindPopup(`
            <div style="font-family:system-ui; color:#0f172a; padding:4px;">
              <strong style="color:#1e3a8a; font-size:13px;">📍 ${topResult.display_name.split(',')[0]}</strong><br>
              <small style="color:#64748b;">${topResult.display_name}</small><br>
              <div style="margin-top:6px; display:flex; gap:4px;">
                <a href="https://www.google.com/maps/dir/?api=1&destination=${lat},${lon}" target="_blank" style="color:#2563eb; font-weight:700; font-size:11px;">🧭 Navigate Here</a>
              </div>
            </div>
          `).openPopup();

          showNotification(`Found: ${topResult.display_name.split(',')[0]}, Tamil Nadu`, 'success');
        } else {
          showNotification(`No Tamil Nadu locations found for "${q}". Try another town or taluk.`, 'warning');
        }
      } catch (err) {
        showNotification('Geocoding request failed. Filter markers locally.', 'error');
      } finally {
        searchBtn.textContent = originalText;
        searchBtn.disabled = false;
      }
    }

    function setupSearchAndFilters() {
      const searchInput = document.getElementById('mapSearchInput');
      const searchBtn = document.getElementById('btnGeocodeSearch');

      searchBtn.addEventListener('click', () => {
        performGeocodeSearch(searchInput.value);
      });

      searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          performGeocodeSearch(searchInput.value);
        }
      });

      // Hospital District Filter
      const hospFilter = document.getElementById('hospitalDistrictFilter');
      if (hospFilter) {
        hospFilter.addEventListener('change', (e) => {
          renderHospitalsView(e.target.value);
        });
      }

      // Shelter District Filter
      const shelterFilter = document.getElementById('shelterDistrictFilter');
      if (shelterFilter) {
        shelterFilter.addEventListener('change', (e) => {
          renderSheltersView(null, e.target.value);
        });
      }
    }
"""

# Inject setupSearchAndFilters into DOMContentLoaded
content = content.replace("setupDistrictSelector();", "setupDistrictSelector();\n      setupSearchAndFilters();")

# Inject the geocode_and_filter_js helper functions before setupRoleSwitcher
content = content.replace("function setupRoleSwitcher() {", geocode_and_filter_js + "\n    function setupRoleSwitcher() {")

# Update renderHospitalsView to accept district filter
old_render_hosp = """    // 1. Hospital View
    function renderHospitalsView() {
      const grid = document.getElementById('hospitalsCardsGrid');
      grid.innerHTML = state.hospitals.map(hosp => `"""

new_render_hosp = """    // 1. Hospital View with Tamil Nadu District Filtering
    function renderHospitalsView(selectedDistrict = 'all') {
      const grid = document.getElementById('hospitalsCardsGrid');
      let list = state.hospitals;
      if (selectedDistrict && selectedDistrict !== 'all') {
        list = list.filter(h => h.district === selectedDistrict);
      }
      grid.innerHTML = list.map(hosp => `"""

content = content.replace(old_render_hosp, new_render_hosp)

# Update renderSheltersView to accept district filter
old_render_shelter = """    // 2. Shelters View
    function renderSheltersView() {
      const grid = document.getElementById('sheltersCardsGrid');
      let filtered = state.shelters;

      if (currentShelterFilter === 'women') filtered = filtered.filter(s => s.womenOnly);
      if (currentShelterFilter === 'pets') filtered = filtered.filter(s => s.petFriendly);
      if (currentShelterFilter === 'medical') filtered = filtered.filter(s => s.medicalSupport);
      if (currentShelterFilter === 'wheelchair') filtered = filtered.filter(s => s.wheelchair);"""

new_render_shelter = """    // 2. Shelters View with Category and District Filtering
    function renderSheltersView(overrideCatFilter = null, selectedDistrict = 'all') {
      const grid = document.getElementById('sheltersCardsGrid');
      const cat = overrideCatFilter || currentShelterFilter;
      let filtered = state.shelters;

      if (selectedDistrict && selectedDistrict !== 'all') {
        filtered = filtered.filter(s => s.district === selectedDistrict);
      }

      if (cat === 'women') filtered = filtered.filter(s => s.womenOnly);
      if (cat === 'pets') filtered = filtered.filter(s => s.petFriendly);
      if (cat === 'medical') filtered = filtered.filter(s => s.medicalSupport);
      if (cat === 'wheelchair') filtered = filtered.filter(s => s.wheelchair);"""

content = content.replace(old_render_shelter, new_render_shelter)

with open("static/index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated static/index.html and index.html (Length: {len(content)} chars)")
