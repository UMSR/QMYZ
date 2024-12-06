import qm_utils.qm as qm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-u", "--url", help="登录URL"
)
parser.add_argument("-c", "--csv", help="题库csv路径")
parser.add_argument("-i", "--course", help="课程id")
parser.add_argument("-n", "--num", help="答题量", default=0, type=int)

args = parser.parse_args()
if args.url is None:
    print("请填写登录URL")
    exit(1)
if args.csv is None:
    print("请填写题库csv路径")
    exit(1)
if args.course is None:
    print("请填写课程id")
    exit(1)
url=args.url
csv=args.csv
course=args.course
num=args.num
ti = qm.qm_tiku(csv)
qm = qm.qm_auto(url,ti.tiku,course)
qm.auto_do(num)
