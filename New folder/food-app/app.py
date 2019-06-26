from flask import Flask, render_template

app = Flask (__name__)

all_foods = [
        {"title": "Bún đậu",
        "description": "Rất ngon",
        "type": "food",
        "link": "https://justfly.vn/Upload/2018/04/bun-dau-mam-tom-25_04_2018_12_53.png"
        },

        {"title": "Thịt rán",
        "description": "Bình thường",
        "type": "food",
        "link": "https://giadinh.tv/wp-content/uploads/2018/10/Cach-lam-mon-thit-ran-ngon_1.jpg"
        },
        
        {"title": "Phở",
        "description": "Tuyệt",
        "type": "drink",
        "link": "https://cdn.tgdd.vn/Files/2018/06/14/1095399/huong-dan-chi-tiet-cach-nau-pho-bo-thom-ngon-bo-duong-cho-ca-nha.png"
        }
    ]

@app.route("/foods")
def home():
    return render_template("all_food.html", ALL_FOODS=all_foods)

@app.route("/foods/<int:index>")
def food_detail(index):
    food =all_foods[index]
    return render_template("food_detail.html", FOOD=food)

if __name__ == "__main__":
    app.run(debug=True)
