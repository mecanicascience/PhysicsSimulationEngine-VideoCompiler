import json
import sys
import os
import glob

from binascii import a2b_base64


def setup(fileName):
    print(
          "\nStarting video creation algorithm. This only works with the blocking frame option set in pSEngine."
        + "\nThere are 3 steps in order to complete this."
        + "\nPlease do not quit until everything is done or there might by issues on your final video."
        + "\nMore infos on pSEngine at 'pSEngine.mecanicascience.fr' (copyright : 2020 - MecanicaScience)"
    )

    # Open the current recorder file
    jsonDatas = openRecorderFile(fileName)

    # Encoded string to PNG image stored in 'raw/' folder
    convertStringToPNG(jsonDatas['datas']['pixels']['pixelDatas'])

    # Create video from the set of every created images
    createVideoFromImageSet(
        jsonDatas['config']['drawFrameCount'],
        jsonDatas['config']['width'],
        jsonDatas['config']['height']
    )

    print(
          "\n\nEnd of program."
        + "\nVideo has correctly been created in 'datas/output.mp4'."
    )





def openRecorderFile(fileName):
    print("\n\n===== Opening and formating file " + "datas/" + fileName + ".json" + " (1/3) =====\n...")
    f = open('datas/' + fileName + '.json', 'r')
    jsonContent = json.loads(f.read())
    print("===== END Opening and formating file (1/3) =====")

    return jsonContent


def convertStringToPNG(dataArray):
    print("\n\n===== Processing images (2/3) =====")
    for i in range(-1, len(dataArray)):
        print("Processing image " + str(i + 1) + '/' + str(len(dataArray)))

        if (dataArray[i][len(dataArray[i]) - 1] == '='):
            j = len(dataArray[i])
            while True:
                j -= 1
                if (dataArray[i][j] != '='):
                    break
            cleanStr = dataArray[i][:-(len(dataArray[i])-j-1)]
        else:
            cleanStr = dataArray[i]

        binary_data = a2b_base64((cleanStr + "=" * 4).split('data:image/png;base64,')[1])

        fd = open('raw/image_' + '{:06d}'.format(i) + '.png', 'wb')
        fd.write(binary_data)
        fd.close()

    print("===== END Processing images (2/3) =====")



def createVideoFromImageSet(FPS, width, height):
    print("\n\n===== Generating video from the set of images (3/3) =====\n...")

    # FFMPEG
    os.system('ffmpeg -r {0} -s {1}x{2} -i raw/image_%06d.png -vcodec libx264 -y -an datas/output.mp4 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2"'.format(FPS, width, height))

    # Delete files in raw
    files = glob.glob('raw/*')
    for f in files:
        os.remove(f)

    print("===== END Generating video from the set of images (3/3) =====")





if __name__ == "__main__":
    if len(sys.argv) <= 1:
        exit("Too less arguments calling script. You need to send the recorder JSON file name.")

    setup(sys.argv[1])
