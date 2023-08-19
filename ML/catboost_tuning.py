from optuna.samplers import TPESampler
import optuna
from utils.models_quality import cross_val
from catboost import CatBoostClassifier


def objective(trial):
    cbc = CatBoostClassifier(
        task_type="GPU",
        devices='0:1',
        learning_rate=trial.suggest_float("learning_rate", 1e-3, 1e-1, log=True),
        depth=trial.suggest_int("depth", 4, 10),
        od_type=trial.suggest_categorical("od_type", ["IncToDec", "Iter"]),
        verbose=False
    )
    return cross_val(df, cbc).mean()


def tune(objective, number_of_trials):
    optuna.logging.set_verbosity(optuna.logging.WARNING)

    sampler = TPESampler(seed=1)
    study = optuna.create_study(study_name="catboost", direction="maximize", sampler=sampler)
    study.optimize(objective, n_trials=number_of_trials)

    print("Number of finished trials: ", len(study.trials))
    print("Best trial:")
    trial = study.best_trial
    print("  Value: ", trial.value)
    print("  Params: ")
    for key, value in trial.params.items():
        print("    {}: {}".format(key, value))
