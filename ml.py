# 1

import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt
import uuid

# 2

x_age = np.arange(0, 101, 1)
x_systolicBP = np.arange(0, 200, 1)
x_diastolicBP = np.arange(0, 150, 1)
x_troponin = np.arange(0, 13, 1)
x_chestpainandpainilefthandnadjaw = np.arange(1, 5, 1)
x_ECG = np.arange(1, 4, 1)
y_risk = np.arange(0, 46, 1)


def calculate(input_age, input_systolicBP, input_diastolicBP, input_troponin, input_chestpainandpainilefthandnadjaw, input_ECG):

    print("\n\nCalculations are being made....\n\n")

    age_young = mf.trapmf(x_age, [-30, -5, 30, 40])
    age_mid = mf.trapmf(x_age, [30, 40, 50, 60])
    age_old = mf.trapmf(x_age, [50, 60, 100, 100])

    systolicBP_low = mf.trapmf(x_systolicBP, [-30, -5, 100, 120])
    systolicBP_mid = mf.trapmf(x_systolicBP, [100, 120, 140, 160])
    systolicBP_high = mf.trapmf(x_systolicBP, [140, 160, 180, 200])
    systolicBP_veryHigh = mf.trapmf(x_systolicBP, [180, 200, 220, 220])

    diastolicBP_low = mf.trapmf(x_diastolicBP, [-30, -5, 30, 50])
    diastolicBP_mid = mf.trapmf(x_diastolicBP, [30, 50, 70, 90])
    diastolicBP_high = mf.trapmf(x_diastolicBP, [70, 90, 100, 120])

    troponin_low = mf.trimf(x_troponin, [-1, 0, 3])
    troponin_normal = mf.trimf(x_troponin, [2, 4, 6])
    troponin_high = mf.trimf(x_troponin, [5, 6, 8])

    chestpainandpainilefthandnadjaw_low = mf.trimf(
        x_chestpainandpainilefthandnadjaw, [-1, 0, 2])
    chestpainandpainilefthandnadjaw_mid = mf.trimf(
        x_chestpainandpainilefthandnadjaw, [0, 2, 3])
    chestpainandpainilefthandnadjaw_high = mf.trimf(
        x_chestpainandpainilefthandnadjaw, [2, 3, 3])

    ECG_normal = mf.trimf(x_ECG, [0, 1, 2,])
    ECG_abnormal = mf.trimf(x_ECG, [1.5, 2, 3,])

    risk_not = mf.trapmf(y_risk, [0, 0, 5, 10])
    risk_little = mf.trapmf(y_risk, [5, 10, 15, 20])
    risk_mid = mf.trapmf(y_risk, [15, 20, 25, 30])
    risk_high = mf.trapmf(y_risk, [25, 30, 35, 40])
    risk_veryHigh = mf.trapmf(y_risk, [35, 40, 45, 50])

    # 6

    fig, (ax0, ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(
        nrows=7, figsize=(10, 25))

    ax0.plot(x_age, age_young, 'r', linewidth=2, label='Young')
    ax0.plot(x_age, age_mid, 'g', linewidth=2, label='Middle')
    ax0.plot(x_age, age_old, 'b', linewidth=2, label='Old')
    ax0.set_title('age')
    ax0.legend()

    ax1.plot(x_systolicBP, systolicBP_low, 'r', linewidth=2, label='Low')
    ax1.plot(x_systolicBP, systolicBP_mid, 'g', linewidth=2, label='Middle')
    ax1.plot(x_systolicBP, systolicBP_high, 'b', linewidth=2, label='High')
    ax1.plot(x_systolicBP, systolicBP_veryHigh,
             'y', linewidth=2, label='Very High')
    ax1.set_title('Systolic_BP')
    ax1.legend()

    ax2.plot(x_diastolicBP, diastolicBP_low, 'r', linewidth=2, label='Low')
    ax2.plot(x_diastolicBP, diastolicBP_mid, 'g', linewidth=2, label='Middle')
    ax2.plot(x_diastolicBP, diastolicBP_high, 'b', linewidth=2, label='High')
    ax2.set_title('Diastolic_BP')
    ax2.legend()

    ax3.plot(x_troponin, troponin_low, 'r', linewidth=2, label='Low')
    ax3.plot(x_troponin, troponin_normal, 'g', linewidth=2, label='Normal')
    ax3.plot(x_troponin, troponin_high, 'b', linewidth=2, label='High')
    ax3.set_title('Troponin-I')
    ax3.legend()

    ax4.plot(x_chestpainandpainilefthandnadjaw,
             chestpainandpainilefthandnadjaw_low, 'r', linewidth=2, label='Low')
    ax4.plot(x_chestpainandpainilefthandnadjaw,
             chestpainandpainilefthandnadjaw_mid, 'g', linewidth=2, label='Middle')
    ax4.plot(x_chestpainandpainilefthandnadjaw,
             chestpainandpainilefthandnadjaw_high, 'b', linewidth=2, label='High')
    ax4.set_title('Chestpain_and_Pain_in_lefthandnadjaw')
    ax4.legend()

    ax5.plot(x_ECG, ECG_normal, 'r', linewidth=2, label='Normal')
    ax5.plot(x_ECG, ECG_abnormal, 'g', linewidth=2, label='Abnormal')
    ax5.set_title('ECG')
    ax5.legend()

    ax6.plot(y_risk, risk_not, 'r', linewidth=2, label='Not')
    ax6.plot(y_risk, risk_little, 'g', linewidth=2, label='Little')
    ax6.plot(y_risk, risk_mid, 'b', linewidth=2, label='Middle')
    ax6.plot(y_risk, risk_high, 'y', linewidth=2, label='High')
    ax6.plot(y_risk, risk_veryHigh, 'm', linewidth=2, label='Very High')
    ax6.set_title('Risk')
    ax6.legend()

    # plt.tight_layout()

    # 7

    age_fit_young = fuzz.interp_membership(x_age, age_young, input_age)
    age_fit_mid = fuzz.interp_membership(x_age, age_mid, input_age)
    age_fit_old = fuzz.interp_membership(x_age, age_old, input_age)

    systolicBP_fit_low = fuzz.interp_membership(
        x_systolicBP, systolicBP_low, input_systolicBP)
    systolicBP_fit_mid = fuzz.interp_membership(
        x_systolicBP, systolicBP_mid, input_systolicBP)
    systolicBP_fit_high = fuzz.interp_membership(
        x_systolicBP, systolicBP_high, input_systolicBP)
    systolicBP_fit_veryHigh = fuzz.interp_membership(
        x_systolicBP, systolicBP_veryHigh, input_systolicBP)

    diastolicBP_fit_low = fuzz.interp_membership(
        x_diastolicBP, diastolicBP_low, input_diastolicBP)
    diastolicBP_fit_mid = fuzz.interp_membership(
        x_diastolicBP, diastolicBP_mid, input_diastolicBP)
    diastolicBP_fit_high = fuzz.interp_membership(
        x_diastolicBP, diastolicBP_high, input_diastolicBP)

    troponin_fit_low = fuzz.interp_membership(
        x_troponin, troponin_low, input_troponin)
    troponin_fit_normal = fuzz.interp_membership(
        x_troponin, troponin_normal, input_troponin)
    troponin_fit_high = fuzz.interp_membership(
        x_troponin, troponin_high, input_troponin)

    chestpainandpainilefthandnadjaw_fit_low = fuzz.interp_membership(
        x_chestpainandpainilefthandnadjaw, chestpainandpainilefthandnadjaw_low, input_chestpainandpainilefthandnadjaw)
    chestpainandpainilefthandnadjaw_fit_mid = fuzz.interp_membership(
        x_chestpainandpainilefthandnadjaw, chestpainandpainilefthandnadjaw_mid, input_chestpainandpainilefthandnadjaw)
    chestpainandpainilefthandnadjaw_fit_high = fuzz.interp_membership(
        x_chestpainandpainilefthandnadjaw, chestpainandpainilefthandnadjaw_high, input_chestpainandpainilefthandnadjaw)

    ECG_fit_normal = fuzz.interp_membership(x_ECG, ECG_normal, input_ECG)
    ECG_fit_abnormal = fuzz.interp_membership(x_ECG, ECG_abnormal, input_ECG)

    # 8

    rule1 = np.fmin(np.fmin(np.fmin(np.fmin(systolicBP_fit_low, diastolicBP_fit_low),
                    troponin_fit_normal), chestpainandpainilefthandnadjaw_fit_low), risk_not)
    rule2 = np.fmin(np.fmin(np.fmin(np.fmin(systolicBP_fit_low, diastolicBP_fit_low),
                    troponin_fit_low), chestpainandpainilefthandnadjaw_fit_mid), risk_little)
    rule3 = np.fmin(np.fmin(np.fmin(np.fmin(systolicBP_fit_low, diastolicBP_fit_low),
                    troponin_fit_low), chestpainandpainilefthandnadjaw_fit_high), risk_mid)
    rule4 = np.fmin(np.fmin(np.fmin(np.fmin(systolicBP_fit_low, diastolicBP_fit_low),
                    troponin_fit_high), chestpainandpainilefthandnadjaw_fit_high), risk_high)
    rule5 = np.fmin(np.fmin(np.fmin(systolicBP_fit_mid,
                    diastolicBP_fit_low), troponin_fit_normal), risk_not)

    rule6 = np.fmin(np.fmin(
        np.fmin(age_fit_young, systolicBP_fit_mid), diastolicBP_fit_mid), risk_not)
    rule7 = np.fmin(np.fmin(np.fmin(age_fit_mid, systolicBP_fit_mid),
                    diastolicBP_fit_mid), risk_not)
    rule8 = np.fmin(np.fmin(np.fmin(age_fit_old, systolicBP_fit_mid),
                    diastolicBP_fit_mid), risk_not)
    rule9 = np.fmin(np.fmin(
        np.fmin(age_fit_young, systolicBP_fit_high), diastolicBP_fit_high), risk_mid)
    rule10 = np.fmin(np.fmin(
        np.fmin(age_fit_mid, systolicBP_fit_high), diastolicBP_fit_high), risk_high)
    rule11 = np.fmin(np.fmin(np.fmin(age_fit_old, systolicBP_fit_high),
                             diastolicBP_fit_high), risk_veryHigh)

    rule12 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_young, systolicBP_fit_mid),
                                             diastolicBP_fit_low), troponin_fit_normal), ECG_fit_normal), risk_not)
    rule13 = np.fmin(np.fmin(age_fit_young, troponin_fit_low), risk_little)
    rule14 = np.fmin(np.fmin(age_fit_mid, troponin_fit_high), risk_high)
    rule15 = np.fmin(np.fmin(age_fit_old, troponin_fit_high), risk_veryHigh)
    rule16 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_young, systolicBP_fit_low), diastolicBP_fit_low),
                                             troponin_fit_low), chestpainandpainilefthandnadjaw_fit_mid), ECG_fit_normal), risk_little)
    rule17 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_mid, systolicBP_fit_low), diastolicBP_fit_low),
                                             troponin_fit_high), chestpainandpainilefthandnadjaw_fit_mid), ECG_fit_abnormal), risk_high)
    rule18 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_old, systolicBP_fit_low), diastolicBP_fit_low),
                                             troponin_fit_high), chestpainandpainilefthandnadjaw_fit_high), ECG_fit_abnormal), risk_veryHigh)
    rule19 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_mid, systolicBP_fit_low), diastolicBP_fit_low),
                                             troponin_fit_high), chestpainandpainilefthandnadjaw_fit_high), ECG_fit_abnormal), risk_veryHigh)

    rule20 = np.fmin(np.fmin(np.fmin(np.fmin(systolicBP_fit_veryHigh,
                                             diastolicBP_fit_high), ECG_fit_abnormal), troponin_fit_high), risk_veryHigh)
    rule21 = np.fmin(np.fmin(np.fmin(np.fmin(systolicBP_fit_high, diastolicBP_fit_high),
                                     ECG_fit_abnormal), troponin_fit_high), risk_veryHigh)
    rule22 = np.fmin(np.fmin(np.fmin(np.fmin(np.fmin(age_fit_young, systolicBP_fit_veryHigh),
                                             diastolicBP_fit_high), ECG_fit_normal), troponin_fit_low), risk_mid)
    rule23 = np.fmin(
        np.fmin(age_fit_mid, systolicBP_fit_veryHigh), risk_veryHigh)
    rule24 = np.fmin(
        np.fmin(age_fit_old, systolicBP_fit_veryHigh), risk_veryHigh)

    # 9

    out_not = np.fmax(
        np.fmax(np.fmax(np.fmax(np.fmax(rule1, rule5), rule6), rule7), rule8), rule12)
    out_little = np.fmax(np.fmax(rule2, rule13), rule16)
    out_mid = np.fmax(np.fmax(rule3, rule9), rule22)
    out_high = np.fmax(np.fmax(np.fmax(rule4, rule10), rule14), rule17)
    out_veryHigh = np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(np.fmax(
        np.fmax(rule11, rule15), rule18), rule19), rule20), rule21), rule23), rule24)

    # 10

    risk0 = np.zeros_like(y_risk)

    fig, ax0 = plt.subplots(figsize=(7, 4))
    ax0.fill_between(y_risk, risk0, out_not, facecolor='r', alpha=0.7)
    ax0.plot(y_risk, risk_not, 'r', linestyle='--')
    ax0.fill_between(y_risk, risk0, out_little, facecolor='g', alpha=0.7)
    ax0.plot(y_risk, risk_little, 'g', linestyle='--')
    ax0.fill_between(y_risk, risk0, out_mid, facecolor='b', alpha=0.7)
    ax0.plot(y_risk, risk_mid, 'b', linestyle='--')
    ax0.fill_between(y_risk, risk0, out_high, facecolor='y', alpha=0.7)
    ax0.plot(y_risk, risk_high, 'y', linestyle='--')
    ax0.fill_between(y_risk, risk0, out_veryHigh, facecolor='m', alpha=0.7)
    ax0.plot(y_risk, risk_veryHigh, 'm', linestyle='--')
    ax0.set_title('Out of the Risk')

    # plt.tight_layout()

    # 11

    out_risk = np.fmax(
        np.fmax(np.fmax(np.fmax(out_not, out_little), out_mid), out_high), out_veryHigh)

    defuzzified = fuzz.defuzz(y_risk, out_risk, 'centroid')

    result = fuzz.interp_membership(y_risk, out_risk, defuzzified)

    print("Coroner Heart Diagnosis:", defuzzified)

    # 12

    fig, ax0 = plt.subplots(figsize=(7, 4))

    ax0.plot(y_risk, risk_not, 'r', linewidth=0.5, linestyle='--')
    ax0.plot(y_risk, risk_little, 'g', linewidth=0.5, linestyle='--')
    ax0.plot(y_risk, risk_mid, 'b', linewidth=0.5, linestyle='--')
    ax0.plot(y_risk, risk_high, 'y', linewidth=0.5, linestyle='--')
    ax0.plot(y_risk, risk_veryHigh, 'm', linewidth=0.5, linestyle='--')

    ax0.fill_between(y_risk, risk0, out_risk, facecolor='Orange', alpha=0.7)
    ax0.plot([defuzzified, defuzzified], [0, result],
             'k', linewidth=1.5, alpha=0.9)
    ax0.set_title('Centroid Deffuzification')

    fileName = 'static/'+str(uuid.uuid4())+'.png'
    plt.savefig(fileName)
    # plt.tight_layout()

    return {
        "score": defuzzified,
        "attachment": fileName
    }


# print(calculate(
#     int(input("Age: ")),
#     int(input("SystolicBP: ")),
#     int(input("DiastolicBP: ")),
#     int(input("troponin: ")),
#     int(input("pain: ")),
#     int(input("ECG: ")),
# ))
