from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from spm.portal.api.v1.serializers import ApprovalDetailSerializer, ApproveSerializer
from spm.portal.flows import ApprovalFlow


class ApprovalFlowMixin:
    flow = ApprovalFlow

    @extend_schema(
        request=ApproveSerializer,
        responses={200: ApprovalDetailSerializer},
    )
    @action(detail=True, methods=["patch"])
    def approve(self, request, pk, *args, **kwargs):
        obj = self.get_object()
        serializer = ApproveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.flow(obj).approve(note=serializer.validated_data["note"], reviewer=request.user)
        # return response
        data = ApprovalDetailSerializer(obj, read_only=True, context=self.get_serializer_context()).data
        return Response(data=data, status=status.HTTP_200_OK)

    @extend_schema(
        request=ApproveSerializer,
        responses={200: ApprovalDetailSerializer},
    )
    @action(detail=True, methods=["patch"])
    def reject(self, request, pk, *args, **kwargs):
        obj = self.get_object()
        serializer = ApproveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.flow(obj).reject(note=serializer.validated_data["note"], reviewer=request.user)
        # return response
        data = ApprovalDetailSerializer(obj, read_only=True, context=self.get_serializer_context()).data
        return Response(data=data, status=status.HTTP_200_OK)
