class BatteryDecisionEngine:

    def evaluate(self, soh, rul):

        if soh > 0.9:
            health = "GOOD"
            charging = "FAST_CHARGE_ALLOWED"
            risk = "LOW"

        elif soh > 0.75:
            health = "MODERATE"
            charging = "NORMAL_CHARGE"
            risk = "MEDIUM"

        else:
            health = "POOR"
            charging = "SLOW_CHARGE_ONLY"
            risk = "HIGH"

        if rul < 40:
            charging = "OFF_PEAK_CHARGING_RECOMMENDED"

        return {
            "SOH": round(soh, 3),
            "RUL": int(rul),
            "Health_Status": health,
            "Charging_Action": charging,
            "Risk_Level": risk
        }