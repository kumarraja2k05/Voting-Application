import session.registration as r
from utilities.utility import Util as Util
import datetime
from tabulate import tabulate
from utilities.colprint.colprint import NewPrint as col



class AllOperation:

    # jab election start honge tab voteRecord table clear kri jayegi, to store votes for current new election
    # jab election end honge tab voteRecord se votes count hoke, result table main update kiye jayenege
    def check_on_going_elections(admin_id):
        sql_command = Util.get_sql_command("ELECTION_STATUS").format(datetime.date.today().year)
        result = Util.fetch_data(sql_command)
        if len(result) == 0:
            col.col_print(
                f"\n---Elections of {datetime.date.today().year} are not yet started---\n", "red")
        elif result[0][0] == 1:
            col.col_print(
                f"\n---Yes Elections of {datetime.date.today().year} are going on---\n", "green")
        else:
            col.col_print(
                f"\n---No Elections of {datetime.date.today().year} are over---\n", "red")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def start_election(admin_id):
        cur_year = datetime.date.today().year
        sql_command = Util.get_sql_command("ELECTION_STATUS").format(cur_year)
        result = Util.fetch_data(sql_command)
        if len(result) != 0:
            if result[0][0] == 2:
                col.col_print(
                    f"\n---Elections of {cur_year} are over---\n", "red")
                return True
            else:
                col.col_print(
                    f'\n---Elections of {cur_year} have already been started---\n', "red")
                return True

        sql_command = Util.get_sql_command("ADD_ELECTION").format(cur_year,1)
        Util.write_data(sql_command)
        sql_command = "call DelVoteRecord"
        Util.write_data(sql_command)
        col.col_print(f"\n---Elections of {cur_year} have begun---\n", "green")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def close_elections(admin_id):
        cur_year = datetime.date.today().year
        sql_command = Util.get_sql_command("ELECTION_STATUS").format(cur_year)
        result = Util.fetch_data(sql_command)
        if len(result) == 0:
            col.col_print(
                f'\n---Elections of {cur_year} have not been started yet---\n', "red")
        elif result[0][0] == 1:
            sql_command = Util.get_sql_command("CLOSE_ELECTIONS").format(cur_year)
            Util.write_data(sql_command)
            AllOperation.fetch_and_store_results(cur_year)
            col.col_print(
                f'\n---Elections of {cur_year} have been closed---\n', "green")
        elif result[0][0] == 2:
            col.col_print(
                f'\n---Elections of {cur_year} have already been closed---\n', "red")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def fetch_and_store_results(year):
        sql_command = Util.get_sql_command("SELECT_ALL").format("Party")
        all_parties = Util.fetch_data(sql_command)
        winning_parties = []
        max_votes = 0
        for i in all_parties:
            cur_party = i[0]
            party_name = i[1]
            # print(cur_party)
            sql_command = Util.get_sql_command("COUNT_VOTE_RECORD").format(cur_party)
            no_of_votes = Util.fetch_data(sql_command)[0][0]
            # print(no_of_votes)
            if no_of_votes == max_votes:
                winning_parties.append(party_name)
            elif no_of_votes > max_votes:
                winning_parties.clear()
                winning_parties.append(party_name)
                max_votes = no_of_votes
            sql_command = Util.get_sql_command("ADD_ELECTION_RESULT").format(cur_party,year,no_of_votes)
            Util.write_data(sql_command)
        col.col_print(
            f"\n---Here's the list of parties with maximum votes : {max_votes}---\n", "green")
        for i in winning_parties:
            print(i, end="\n")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def add_party(admin_id):
        party_name = input("Enter the name of the Party : ")
        party_id = Util.get_number_of_records("Party")[0][0]+1
        sql_command = Util.get_sql_command("ADD_PARTY").format(party_id, party_name)
        try:
            Util.write_data(sql_command)
        except:
            col.col_print("\n---Party already exists---\n", "red")
        else:
            col.col_print(
                f"\n---Successfully added the party '{party_name}'---\n", "green")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def give_vote(user_id):
        cur_year = datetime.date.today().year
        sql_command = Util.get_sql_command("ELECTION_STATUS").format(cur_year)
        result = Util.fetch_data(sql_command)
        if len(result) == 0:
            col.col_print(
                f'\n---Elections of {cur_year} have not been started yet---\n', "red")
        elif result[0][0] == 1:
            sql_command = Util.get_sql_command("GET_USER_VOTE_RECORD").format(user_id)        
            has_voted = Util.fetch_data(sql_command)
            if len(has_voted) != 0:
                col.col_print("\n---You have already voted !---\n", "green")
                return True
            sql_command = Util.get_sql_command("SELECT_ALL").format("Party")
            result = Util.fetch_data(sql_command)
            all_parties_list=[]
            for i in result:
                all_parties_list.append([i[0],i[1]])
            print(tabulate(all_parties_list, headers=["Party Number", "Party Name"], tablefmt='fancy_grid'))
            voter_choice = input("Enter the party of your choice : ")
            while not (voter_choice.isdigit() and int(voter_choice) >= 1 and int(voter_choice) <= len(result)):
                col.col_print("Invalid party Id, try again", "red")
                voter_choice = input("Enter the party of your choice : ")
            sql_command = Util.get_sql_command("GIVE_VOTE").format(user_id, 1, voter_choice)
            Util.write_data(sql_command)
            col.col_print("\n---Successfuly voted---\n","green")
        elif result[0][0] == 2:
            col.col_print(
                f'\n---Elections of {cur_year} have already been closed---\n', "red")
        return True

# -------------------------------------------------------------------------------------------------------------------------------------

    def results(admin_id):
        # will show the result of past elections.
        year = input(
            "\nEnter the Election year whose result is to be displayed : ")
        try:
            year = int(year)
        except:
            col.col_print("\n---Opps, Invalid year, try again---\n", "red")
            AllOperation.results(admin_id)
        else:
            sql_command = Util.get_sql_command("PREV_RESULT").format(year)
            result = Util.fetch_data(sql_command)
            if len(result) == 0:
                col.col_print(
                    f"\n---No record found for year {year}---\n", "red")
                return True
            col.col_print(
                "\n---Showing Party names and their votes---", "green")
            res=[]
            for i in result:
                res.append([i[0],i[1]])
            print(tabulate(res, headers=["Party", "Votes"], tablefmt='fancy_grid'))
            print("\n")
        return True
