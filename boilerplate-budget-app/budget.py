import math

class Category(object):
    def __init__(self, cat):

        self.ledger = []
        self.cat = cat
        self.balance = 0

    def get_balance(self):

        return self.balance

    def deposit(self, amount, description = None):

        amount = float(amount)

        if description:
            dict = {"amount" : amount, "description" : description}

        else:
            dict = {"amount" : amount, "description" : ""}

        self.ledger.append(dict)
        self.balance += amount

    def check_funds(self, amount_checked):

        if amount_checked > self.balance:
            return False

        else:
            return True

    def withdraw(self, amount, description = None):

        amount = float(amount)

        if description:
            dict = {"amount" : -amount, "description" : description}

        else:
            dict = {"amount" : -amount, "description" : ""}

        if self.check_funds(amount) is True:
            self.balance -= amount
            self.ledger.append(dict)

            return True

        else:
            return False

    def transfer(self, amount_transfer, to_cat):

        amount_transfer = float(amount_transfer)
        descr_to_transfer = f"Transfer to {to_cat.cat}"
        descr_from_transfer = f"Transfer from {self.cat}"

        if self.check_funds(amount_transfer) is True:
            self.withdraw(amount_transfer, descr_to_transfer)
            to_cat.deposit(amount_transfer, descr_from_transfer)

            return True

        else:
            return False

    def __str__(self):

        nr_stars = 30 - int(len(self.cat))

        if nr_stars % 2 == 0:
            nr_stars = nr_stars / 2
            stars = "*" * int(nr_stars)

            title = f"{stars}{str(self.cat)}{stars}"

        else:
            nr_stars = nr_stars / 2
            stars_left = "*" * int(nr_stars - 0.5)
            stars_right = "*" * int(nr_stars + 0.5)

            title = f"{stars_left}{str(self.cat)}{stars_right}"

        out_description = ""
        content = ""
        out_amount = 0
        total = 0

        for dict_list in self.ledger:

            for key, value in dict_list.items():

                if key == "amount":
                    out_amount = value
                    out_amount = "%0.2f" % out_amount

                    total += float(out_amount)

                else:
                    out_description = str(value)[0:23]

            content += f"{out_description.ljust(23)}{out_amount.rjust(7)}\n"

        output = f"{title}\n{content}Total: {total}"
        return output


def create_spend_chart(list):

    cat_number = len(list)
    temp_number = 0
    w_total = 0
    w_a_list = []

    # Calculate total withdrawals:
    while temp_number < cat_number:

        for cat_name in list:

            for cat_dict in cat_name.ledger:
                if cat_dict["amount"] < 0:
                    # Total withdrawals:
                    w_total += float(cat_dict["amount"]) # 116.58999999999999

                    # Tuples with amounts correlated to their categories:
                    w_amount = (temp_number, cat_dict["amount"])
                    w_a_list.append(w_amount)

            temp_number += 1


    last_tuple = len(w_a_list) - 1
    w_sum_list = []
    nr_tuple = 0
    w_sum = 0

    # Calculate total withdrawals for each category:
    for tuple in w_a_list:
        if nr_tuple == tuple[0]:
            w_sum += tuple[1]

        else:
            w_sum_list.append(w_sum)
            nr_tuple += 1
            w_sum = tuple[1]

        if tuple == w_a_list[last_tuple]:
            w_sum_list.append(w_sum)


    all_bars = []

    # Calculate percentage for each category's total withdrawals:
    for sum in w_sum_list:
        percentage = 10 * (sum / w_total) # 6.5 2.2 1.3
        percentage = math.floor(percentage) # 6 2 1
        bar = percentage + 1
        all_bars.append(bar) # [7, 3, 2]


    bar_list = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]
    white_list = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    all_bars = all_bars
    b_w_list = []
    for each_bar in all_bars:
        w = 11 - int(each_bar)
        b = bar_list[:int(each_bar)] + white_list[:11-each_bar]
        b_w_list.append(b)

    b_w_list.reverse()

    content_list = []

    n = 0
    m = 0
    z = 0
    while m < len(bar_list):

        while n < len(b_w_list):

            if n == (len(all_bars) - 1):
                line = b_w_list[n][m]
                content_list.append(line)
                n = 0
                m += 1

            else:

                if m != len(bar_list):
                    line = b_w_list[n][m]
                    content_list.append(line)
                    n += 1

                else:
                    break

    content_list.reverse()
    xx = 0
    while xx <= (len(content_list) - cat_number): # xx < 33-3

        # Label from 0 to 100:
        labels = ""
        for number in reversed(range(0,101)):
            if number % 10 == 0:
                # Add one whitespace at the end of the row:
                if xx % cat_number == 0:
                    content_list[xx+2] += " "
                content = '  '.join(content_list[xx : xx + cat_number])
                labels += f"{str(number).rjust(3)}| {content} \n"
                xx += 3

    # Output category name:
    yy = 0

    name_list = []
    max = 0
    while yy < cat_number:
        temp_name = list[yy].cat
        lenght_name = len(temp_name)
        name_list.append(temp_name)
        yy += 1
        if max == 0 or max < lenght_name:
            max = lenght_name

    name_list_equal = []
    for nm in name_list:
        if len(nm) < max:
            nm += " " * (max - len(nm))
        else:
            nm = nm
        name_list_equal.append(nm)

    hh = 0
    jj = 0
    f_list = []
    while jj < max: #jj < 8
        while hh < cat_number: # hh < 3
            f = name_list_equal[hh][jj] # 2 0
            f_list.append(f)
            hh += 1
        hh = 0
        jj += 1

    uu = 0
    name_output = ""
    while uu < len(f_list):
        if uu % cat_number == 0:
            f_list[uu+2] += "  "
        name_cat_output = "  ".join(f_list[uu : uu + 3])
        name_output += f"\n     {name_cat_output}"
        uu += 3

    # Number of total categories * 3 (3 dashes for each category),
    # plus 1 because horizontal line below the bars should go two
    # spaces past the final bar.
    dashes = "-" * ((cat_number * 3) + 1)
    title = "Percentage spent by category"
    output = f"{title}\n{labels}    {dashes}{name_output}"
    return output

