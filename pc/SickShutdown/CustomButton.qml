import QtQuick
import QtQuick.Window

Rectangle {
    property string bg
    property string image
    property int _size: 100

   function onClick() {}

    id: base
    visible: true
    width: _size
    height: _size
    color: bg
    radius: 10
    border.width: 0

    MouseArea {
        anchors.fill: base
        hoverEnabled: true

        onEntered: {

        }

        onReleased: {
            onClick()
        }

        Image {
            id: img
            anchors.fill: parent
            source: image
            antialiasing: true
            scale: 0.7
            fillMode: Image.PreserveAspectFit
        }
    }
}



/*##^##
Designer {
    D{i:0;formeditorZoom:3}
}
##^##*/
