
namespace GoogleARCore.Examples.ObjectManipulation
{
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    public class WindowClosed : MonoBehaviour
    {
        private static WindowClosed instance = null;
        public static WindowClosed Instance
        {
            get
            {
                return instance;

            }
        }

        public bool IsClosed = true;

        private void Awake()
        {
            if (instance)
            {
                DestroyImmediate(gameObject.GetComponent<PlaneManager>());
                return;
            }
            instance = this;
        }

        public void Closed()
        {
            IsClosed = true;
        }
    }
}