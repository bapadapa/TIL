using GoogleARCore;
using System.Collections.Generic;
using UnityEngine;

public class ARSurfaceManager : MonoBehaviour
{
	[SerializeField] Material m_surfaceMaterial;
    [SerializeField] List<TrackedPlane> m_newPlanes = new List<TrackedPlane>();

	void Update()
	{
		if (Session.Status != SessionStatus.Tracking)
		{
			return;
		}

		Session.GetTrackables(m_newPlanes, TrackableQueryFilter.New);

		foreach (var plane in m_newPlanes)
		{
			var surfaceObj = new GameObject("ARSurface");
            surfaceObj.transform.parent = this.gameObject.transform;
			var arSurface = surfaceObj.AddComponent<ARSurface>();
			arSurface.SetTrackedPlane(plane, m_surfaceMaterial);
		}
	}
   
}
