# 🩺 Biceop Healthcare & Biometric Telemetry Architecture

## 1. Overview

Biceop pairs training data (sets, weight, reps, RPE) with continuous metabolic and cardiovascular telemetry to understand how workouts impact the human body in real time.

By continuously measuring **Blood Pressure (BP)**, **Blood Glucose (CGM)**, and **Heart Rate Variability (HRV)**, the platform transitions fitness tracking from subjective estimation into data-backed physiological precision.

---

## 2. Telemetry Parameters & Sports Science Applications

```
                  ┌──────────────────────────────┐
                  │    Athlete Biometrics Feed   │
                  └──────────────┬───────────────┘
                                 │
     ┌───────────────────────────┼───────────────────────────┐
     ▼                           ▼                           ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  Blood Pressure  │    │  Blood Glucose   │    │     HRV & HR     │
│   (Vascular)     │    │   (Metabolic)    │    │   (Autonomic)    │
└────────┬─────────┘    └────────┬─────────┘    └────────┬─────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ • Intra-set peak │    │ • Glycemic spike │    │ • CNS Fatigue    │
│   vascular load  │    │   after meals    │    │   scoring        │
│ • Arterial stiff-│    │ • Intra-workout  │    │ • Daily training │
│   ness baseline  │    │   energy dips    │    │   readiness (0-100)
│ • Hypertension   │    │ • Post-workout   │    │ • Heart rate zone│
│   risk screening │    │   carb timing    │    │   transitions    │
└──────────────────┘    └──────────────────┘    └──────────────────┘
```

---

## 3. Metrics Specification

### A. Blood Pressure (Intra-Workout & Resting)
- **Resting Target:** `< 120/80 mmHg` (AHA standard)
- **Workout Monitoring:** Monitors systolic spikes during heavy valsalva maneuvers (e.g. heavy squats/deadlifts) and measures recovery decay rate back to baseline.
- **Protocol:** High-frequency optical PPG pulse transit time combined with calibration offsets.

### B. Continuous Glucose Monitoring (CGM)
- **Sampling Rate:** 1 reading every 1 to 5 minutes via BLE.
- **Intra-Workout Performance Zone:** `90 - 140 mg/dL`.
- **Hypoglycemia Alert:** `< 70 mg/dL` — Triggers in-app prompt recommending fast-acting carbohydrates.
- **Hyperglycemic Spike Analysis:** Evaluates post-prandial glycemic area-under-the-curve (AUC) for pre-workout meals to optimize sustained muscular endurance.

### C. Heart Rate & HRV (Autonomic Recovery)
- **RMSSD / SDNN Metrics:** Measures parasympathetic vs. sympathetic nervous system balance.
- **Readiness Score (0-100):** Weighted combination of morning HRV vs. 30-day baseline, resting heart rate, and previous day total training volume.

---

## 4. Telemetry Data Model (JSON Schema)

```json
{
  "user_id": "usr_9981a",
  "session_id": "ses_push_day_02",
  "timestamp": "2026-09-01T07:30:00Z",
  "telemetry": {
    "blood_pressure": {
      "systolic_mmhg": 124,
      "diastolic_mmhg": 78,
      "measurement_type": "CONTINUOUS_OPTICAL_ESTIMATE"
    },
    "blood_glucose": {
      "value_mg_dl": 108.5,
      "trend_arrow": "FLAT",
      "sensor_source": "BLE_CGM_DEV_01"
    },
    "cardiovascular": {
      "heart_rate_bpm": 138,
      "hrv_rmssd_ms": 48.2,
      "hr_zone": "ZONE_3_AEROBIC"
    },
    "thermal": {
      "skin_temperature_celsius": 34.8
    }
  },
  "context": {
    "activity": "EXERCISE_SET",
    "exercise_name": "Barbell Incline Bench Press",
    "set_number": 3,
    "weight_kg": 95.0,
    "reps_completed": 8,
    "rpe": 8.5
  }
}
```

---

## 5. BLE Connectivity Protocol

The Biceop mobile client connects to standard BLE peripheral GATT services:
- **`0x180D` (Heart Rate):** Real-time pulse and inter-beat intervals (RR-intervals).
- **`0x1808` (Glucose):** Continuous glucose measurement characteristic notifications.
- **`0x1810` (Blood Pressure):** Blood pressure feature and intermediate cuff/optical pressure notifications.
- **Custom Biceop Telemetry GATT Profile (`0xBC01`):** Multiplexed real-time packet for custom high-rate sensor bands.
