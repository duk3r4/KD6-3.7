from modules import albania, bosnia_herzegovina, belgium, bulgaria, denmark, france, estonia, finland, czech_republic, \
    slovakia
import click


@click.group()
def run():
    pass


@click.command()
@click.option('--nin', type=str, help='National Identification Number (Numri i Identitetit (NID)); 10 alphanumerical '
                                      'digits')
def alb(nin):
    albania.alb_alg_nin(nin)


@click.command()
@click.option('--nin', type=str, help='National Identification Number (National Register Number); 11 digits')
@click.option('--icn', type=str, help='Identity Card Number; 9, 10, or 12 digits')
def bel(nin, icn):
    if nin:
        belgium.bel_alg_nin(nin)
    if icn:
        belgium.bel_alg_icn(icn)


@click.command()
@click.option('--nin', type=str, help='National Identification Number (Unique Master Citizen Number '
                                      '(UMCN)/Jedinstveni matični broj (JMB)/Jedinstveni matični broj građana (JMBG)); '
                                      '13 digits')
def bih(nin):
    bosnia_herzegovina.bih_alg_nin(nin)


@click.command()
@click.option('--nin', type=str, help='National Identification Number (Единен граждански номер '
                                      '(ЕГН)/Edinen grazhdanski nomer (EGN)); 10 digits')
def bgr(nin):
    bulgaria.bgr_alg_nin(nin)


@click.command()
@click.option('--nin', type=str, help='National Identification Number (Birth Number/Rodné Číslo (RČ)); 10 or 9 digits')
def cze(nin):
    czech_republic.cze_alg_nin(nin)


@click.command()
@click.option('--nin', type=str, help='National Identification Number (Det Centrale Personregister (CPR-nummer)); '
                                      '10 digits')
def dnk(nin):
    denmark.dnk_alg_nin(nin)


@click.command()
@click.option('--nin', type=str, help='National Identification Number (Isikukood (IK)); 11 digits')
def est(nin):
    estonia.est_alg_nin(nin)


@click.command()
@click.option('--nin', type=str, help='National Identification Number (Henkilötunnus (HETU)); 11 alphanumerical digits')
def fin(nin):
    finland.fin_alg_nin(nin)


@click.command()
@click.option('--nin', type=str, help='National Identification Number (INSEE Code (NIR)); 13 alphanumerical digits')
def fra(nin):
    france.fra_alg_nin(nin)


@click.command()
@click.option('--nin', type=str, help='National Identification Number (Birth Number/Rodné Číslo (RČ))')
def svk(nin):
    slovakia.svk_alg_nin(nin)


run.add_command(alb)
run.add_command(bel)
run.add_command(bih)
run.add_command(bgr)
run.add_command(cze)
run.add_command(dnk)
run.add_command(est)
run.add_command(fin)
run.add_command(fra)
run.add_command(svk)

if __name__ == "__main__":
    run()
